from __future__ import absolute_import

import os
import sys
import unittest
import json
from time import sleep
import tarfile

import epm_client
from epm_client.rest import ApiException
from epm_client.apis.key_api import KeyApi
from epm_client.api_client import ApiClient
from epm_client.models import PoP, ClusterFromResourceGroup
from epm_client.models import CommandExecutionBody


class FullTest(unittest.TestCase):
    """ KeyApi unit test stubs """

    def setUp(self):
        api_client = ApiClient(host="http://<REPLACE>:8180/v1")
        self.key_api = epm_client.apis.key_api.KeyApi(api_client=api_client)
        self.worker_api = epm_client.apis.worker_api.WorkerApi(api_client=api_client)
        self.package_api = epm_client.apis.PackageApi(api_client=api_client)
        self.runtime_api = epm_client.apis.RuntimeApi(api_client=api_client)
        self.adapter_api = epm_client.apis.AdapterApi(api_client=api_client)
        self.pop_api = epm_client.apis.PoPApi(api_client=api_client)
        self.cluster_api = epm_client.apis.ClusterApi(api_client=api_client)

    @unittest.skip
    def test(self):
        #sleep(120)
        adapters = self.adapter_api.get_all_adapters()
        ansible_found = False
        for a in adapters:
            if a.type == "ansible":
                ansible_found = True
        assert ansible_found

        os_pop = PoP( interface_endpoint="<REPLACE>", interface_info=[{"key": "type", "value": "openstack"},
                                                                                   {"key": "username",
                                                                                    "value": "<REPLACE>"},
                                                                                   {"key": "password",
                                                                                    "value": "<REPLACE>"},
                                                                                   {"key": "project_name",
                                                                                    "value": "<REPLACE>"},
                                                                                   {"key": "auth_url",
                                                                                    "value": "<REPLACE>"}], name="os-dc1")
        self.pop_api.register_po_p(os_pop)

        ansible_package = self.package_api.receive_package(file='resources/ansible-package.tar')
        print(ansible_package)

        sleep(15)

        with open('resources/key.json', encoding="UTF-8") as f:
            x = f.read()
            x = x.replace('\n', '\\n')
            print(x)
            data = json.loads(x, strict=False)
        k = self.key_api.add_key(data)

        with open('resources/worker.json') as f:
            data = json.load(f)
        w = self.worker_api.register_worker(data)

        self.worker_api.install_adapter(w.id, "docker")
        self.worker_api.install_adapter(w.id, "docker-compose")

        # LAUNCH COMPOSE PACKAGE
        sleep(10)
        compose_package = self.package_api.receive_package('resources/compose-package.tar')
        assert len(compose_package.vdus) > 0
        command = CommandExecutionBody(command="ls /", await_completion=True)
        self.runtime_api.execute_on_instance(id=compose_package.vdus[0].id, command_execution_body=command)

        # CLEAN
        self.package_api.delete_package(compose_package.id)
        self.worker_api.delete_worker(w.id)
        self.key_api.delete_key(k.id)
        self.package_api.delete_package(ansible_package.id)

        print("Test completed :)")

        print("Test case 1 completed :)")


    ''' 
    
    Test Case 2 - From EPM and EPM Ansible Adapter - Launch a K8s Cluster and add a new node
    
    '''

    @unittest.skip
    def test_case_2(self):
        os_pop = PoP(interface_endpoint="http://<REPLACE>:5000/v2.0",
                     interface_info=[{"key": "type", "value": "openstack"},
                                     {"key": "username",
                                      "value": "<REPLACE>"},
                                     {"key": "password",
                                      "value": "<REPLACE>"},
                                     {"key": "project_name",
                                      "value": "<REPLACE>"},
                                     {"key": "auth_url",
                                      "value": "http://<REPLACE>:5000/v2.0"}], name="os-dc1", status="active")
        self.pop_api.register_po_p(os_pop)

        # sleep(120)
        adapters = self.adapter_api.get_all_adapters()
        ansible_found = False
        for a in adapters:
            if a.type == "ansible":
                ansible_found = True
        assert ansible_found

        ansible_package = self.package_api.receive_package(file='resources/ansible-package2.tar')
        print(ansible_package)

        ansible_package_single = self.package_api.receive_package(file='resources/ansible-package.tar')
        print(ansible_package_single)

        cluster_from_resource_group = ClusterFromResourceGroup(resource_group_id=ansible_package.id, type=["kubernetes"], master_id=ansible_package.vdus[0].id)
        cluster = self.cluster_api.create_cluster(cluster_from_resource_group=cluster_from_resource_group)

        self.cluster_api.add_worker(id=cluster.id, machine_id=ansible_package_single.vdus[0].id)

        print(self.cluster_api.get_all_clusters())

        self.cluster_api.remove_node(id=cluster.id, worker_id=cluster.nodes[0].id)

        print(self.cluster_api.get_all_clusters())

        self.cluster_api.delete_cluster(id=cluster.id)
        self.package_api.delete_package(ansible_package.id)
        self.package_api.delete_package(ansible_package_single.id)
        print("Test case 2 completed :)")

if __name__ == '__main__':
    unittest.main()
