# coding: utf-8

"""
    EPM REST API

    REST API description of the ElasTest Platform Manager Module.

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import epm_client
from epm_client.rest import ApiException
from epm_client.apis.package_api import PackageApi


class TestPackageApi(unittest.TestCase):
    """ PackageApi unit test stubs """

    def setUp(self):
        self.api = epm_client.apis.package_api.PackageApi()

    def tearDown(self):
        pass

    @unittest.skip
    def test_receive_delete_package(self):
        """
        Test case for receive_package

        Receives a package.
        """
        rg = self.api.receive_package("resources/compose-package.tar")
        print(rg)
        self.api.delete_package(rg.to_dict()["id"])
        pass


if __name__ == '__main__':
    unittest.main()
