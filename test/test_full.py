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
from epm_client.models import CommandExecutionBody


class FullTest(unittest.TestCase):
    """ KeyApi unit test stubs """

    def setUp(self):
        api_client = ApiClient(host="http://elastest-epm:8180/v1")
        self.key_api = epm_client.apis.key_api.KeyApi(api_client=api_client)
        self.worker_api = epm_client.apis.worker_api.WorkerApi(api_client=api_client)
        self.package_api = epm_client.apis.PackageApi(api_client=api_client)
        self.runtime_api = epm_client.apis.RuntimeApi(api_client=api_client)
        self.adapter_api = epm_client.apis.AdapterApi(api_client=api_client)
        self.pop_api = epm_client.apis.PoPApi(api_client=api_client)

    def test(self):
        sleep(120)
        adapters = self.adapter_api.get_all_adapters()
        docker_found = False
        for a in adapters:
            if a.type == "docker":
                docker_found = True

        pops = self.pop_api.get_all_po_ps()
        ansible_found = False
        for pop in pops:
            for kvp in pop.interface_info:
                if kvp.key == "type" and kvp.value == "ansible":
                    ansible_found = True
        assert ansible_found
        assert docker_found

        ansible_package = self.package_api.receive_package(file='resources/ansible-package.tar')

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

        # LAUNCH DOCKER PACKAGE
        docker_package = self.package_api.receive_package("resources/docker-package.tar")
        assert len(docker_package.vdus) > 0
        command = CommandExecutionBody(command="ls /", await_completion=True)
        self.runtime_api.execute_on_instance(id=docker_package.vdus[0].id, command_execution_body=command)

        # CLEAN
        self.package_api.delete_package(compose_package.id)
        self.package_api.delete_package(docker_package.id)
        self.worker_api.delete_worker(w.id)
        self.key_api.delete_key(k.id)
        self.package_api.delete_package(ansible_package.id)

        print("Test completed :)")


if __name__ == '__main__':
    unittest.main()

