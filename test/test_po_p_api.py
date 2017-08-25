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
from swagger_client.models import PoP

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.po_p_api import PoPApi


class TestPoPApi(unittest.TestCase):
    """ PoPApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.po_p_api.PoPApi()

    def tearDown(self):
        pass

    def test_get_all_po_ps(self):
        """
        Test case for get_all_po_ps

        Returns all PoPs.
        """
        self.api.get_all_po_ps()
        pass

    def test_get_po_p_by_id(self):
        """
        Test case for get_po_p_by_id

        Returns a PoP.
        """
        self.api.get_po_p_by_id("927ae1d3-89b7-4444-8377-a1e16c890785")
        pass

    def test_register_po_p(self):
        """
        Test case for register_po_p

        Registers a new PoP
        """
        pop = PoP(interface_endpoint="unix:///var/run/docker.sock", name="test")
        self.api.register_po_p(body=pop.to_dict())
        pass

    def test_unregister_po_p(self):
        """
        Test case for unregister_po_p

        Unregisters a PoP.
        """
        self.api.unregister_po_p("ae2c4e87-d145-4e07-a437-7a376a24cea5")
        pass

    def test_update_po_p(self):
        """
        Test case for update_po_p

        Updates a PoP.
        """
        pop = PoP(interface_endpoint="unix:///var/run/docker.sock", name="test")
        self.api.update_po_p("ae2c4e87-d145-4e07-a437-7a376a24cea5", pop.to_dict())
        pass


if __name__ == '__main__':
    unittest.main()
