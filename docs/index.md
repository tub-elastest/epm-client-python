# EPM SDK for python

This repository provides an SDK for python to be used for the ElasTest Platform Manager.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/mpauls/epm-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mpauls/epm-client-python.git`)

Then import the package:
```python
import epm_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import epm_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = epm_client.NetworkApi()
body = epm_client.Network() # Network | Defintion of a Network which has to be created on a certain PoP

try:
    # Creates a new network.
    api_response = api_instance.create_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8180/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NetworkApi* | [**create_network**](NetworkApi.md#create_network) | **POST** /network | Creates a new network.
*NetworkApi* | [**delete_network**](NetworkApi.md#delete_network) | **DELETE** /network/{id} | Deletes a network.
*NetworkApi* | [**get_all_networks**](NetworkApi.md#get_all_networks) | **GET** /network | Returns all existing networks.
*NetworkApi* | [**get_network_by_id**](NetworkApi.md#get_network_by_id) | **GET** /network/{id} | Returns a network.
*NetworkApi* | [**update_network**](NetworkApi.md#update_network) | **PATCH** /network/{id} | Updates a Network.
*PackageApi* | [**delete_package**](PackageApi.md#delete_package) | **DELETE** /packages/{id} | Deletes a package.
*PackageApi* | [**receive_package**](PackageApi.md#receive_package) | **POST** /packages | Receives a package.
*PoPApi* | [**get_all_po_ps**](PoPApi.md#get_all_po_ps) | **GET** /pop | Returns all PoPs.
*PoPApi* | [**get_po_p_by_id**](PoPApi.md#get_po_p_by_id) | **GET** /pop/{id} | Returns a PoP.
*PoPApi* | [**register_po_p**](PoPApi.md#register_po_p) | **POST** /pop | Registers a new PoP
*PoPApi* | [**unregister_po_p**](PoPApi.md#unregister_po_p) | **DELETE** /pop/{id} | Unregisters a PoP.
*PoPApi* | [**update_po_p**](PoPApi.md#update_po_p) | **PATCH** /pop/{id} | Updates a PoP.
*ResourceGroupApi* | [**create_resource_group**](ResourceGroupApi.md#create_resource_group) | **POST** /resourceGroup | Creates a new Resource Group.
*ResourceGroupApi* | [**delete_resource_group**](ResourceGroupApi.md#delete_resource_group) | **DELETE** /resourceGroup/{id} | Deletes a Resource Group.
*ResourceGroupApi* | [**get_all_resource_groups**](ResourceGroupApi.md#get_all_resource_groups) | **GET** /resourceGroup | Returns all Resource Groups.
*ResourceGroupApi* | [**get_resource_group_by_id**](ResourceGroupApi.md#get_resource_group_by_id) | **GET** /resourceGroup/{id} | Returns a Resource Group.
*ResourceGroupApi* | [**update_resource_group**](ResourceGroupApi.md#update_resource_group) | **PATCH** /resourceGroup/{id} | Updates a ResourceGroup.
*RuntimeApi* | [**download_file_from_instance**](RuntimeApi.md#download_file_from_instance) | **GET** /runtime/{id}/file | Downloads a file from a VDU.
*RuntimeApi* | [**execute_on_instance**](RuntimeApi.md#execute_on_instance) | **PUT** /runtime/{id}/action/execute | Executes given command on the given VDU.
*RuntimeApi* | [**start_instance**](RuntimeApi.md#start_instance) | **PUT** /runtime/{id}/action/start | Starts the given VDU.
*RuntimeApi* | [**stop_instance**](RuntimeApi.md#stop_instance) | **PUT** /runtime/{id}/action/stop | Stops the given VDU.
*RuntimeApi* | [**upload_file_to_instance_by_file**](RuntimeApi.md#upload_file_to_instance_by_file) | **POST** /runtime/{id}/file | Uploads a file to a VDU.
*RuntimeApi* | [**upload_file_to_instance_by_path**](RuntimeApi.md#upload_file_to_instance_by_path) | **POST** /runtime/{id}/path | Uploads a file to a VDU.
*TOSCAApi* | [**deploy_tosca_template**](TOSCAApi.md#deploy_tosca_template) | **POST** /tosca | Deploys a Tosca template.
*VDUApi* | [**delete_vdu**](VDUApi.md#delete_vdu) | **DELETE** /vdu/{id} | Terminates a VDU.
*VDUApi* | [**deploy_vdu**](VDUApi.md#deploy_vdu) | **POST** /vdu | Allocates resources in the target cloud.
*VDUApi* | [**get_all_vdus**](VDUApi.md#get_all_vdus) | **GET** /vdu | Returns all VDUs.
*VDUApi* | [**get_vdu_by_id**](VDUApi.md#get_vdu_by_id) | **GET** /vdu/{id} | Returns a VDU.
*VDUApi* | [**update_vdu**](VDUApi.md#update_vdu) | **PATCH** /vdu/{id} | Updates a VDU.


## Documentation For Models

 - [CommandExecutionBody](CommandExecutionBody.md)
 - [Event](Event.md)
 - [FileDownloadBody](FileDownloadBody.md)
 - [FileUploadBody](FileUploadBody.md)
 - [KeyValuePair](KeyValuePair.md)
 - [Network](Network.md)
 - [PoP](PoP.md)
 - [ResourceGroup](ResourceGroup.md)
 - [VDU](VDU.md)


## Documentation For Authorization

 All endpoints do not require authorization.

