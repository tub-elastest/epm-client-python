[![][ElasTest Logo]][ElasTest]

Copyright © 2017-2019 [ElasTest]. Licensed under [Apache 2.0 License].

# EPM client for python

# What is ElasTest

This repository is part of [ElasTest], which is an open source elastic platform
aimed to simplify end-to-end testing. ElasTest platform is based on three
principles: i) Test orchestration: Combining intelligently testing units for
creating a more complete test suite following the “divide and conquer” principle.
ii) Instrumentation and monitoring: Customizing the SuT (Subject under Test)
infrastructure so that it reproduces real-world operational behavior and allowing
to gather relevant information during testing. iii) Test recommendation: Using machine
learning and cognitive computing for recommending testing actions and providing
testers with friendly interactive facilities for decision taking.

# Documentation

The [ElasTest] project provides detailed documentation including tutorials,
installation and development guide.

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
*NetworkApi* | [**create_network**](docs/NetworkApi.md#create_network) | **POST** /network | Creates a new network.
*NetworkApi* | [**delete_network**](docs/NetworkApi.md#delete_network) | **DELETE** /network/{id} | Deletes a network.
*NetworkApi* | [**get_all_networks**](docs/NetworkApi.md#get_all_networks) | **GET** /network | Returns all existing networks.
*NetworkApi* | [**get_network_by_id**](docs/NetworkApi.md#get_network_by_id) | **GET** /network/{id} | Returns a network.
*NetworkApi* | [**update_network**](docs/NetworkApi.md#update_network) | **PATCH** /network/{id} | Updates a Network.
*PoPApi* | [**get_all_po_ps**](docs/PoPApi.md#get_all_po_ps) | **GET** /pop | Returns all PoPs.
*PoPApi* | [**get_po_p_by_id**](docs/PoPApi.md#get_po_p_by_id) | **GET** /pop/{id} | Returns a PoP.
*PoPApi* | [**register_po_p**](docs/PoPApi.md#register_po_p) | **POST** /pop | Registers a new PoP
*PoPApi* | [**unregister_po_p**](docs/PoPApi.md#unregister_po_p) | **DELETE** /pop/{id} | Unregisters a PoP.
*PoPApi* | [**update_po_p**](docs/PoPApi.md#update_po_p) | **PATCH** /pop/{id} | Updates a PoP.
*ResourceGroupApi* | [**create_resource_group**](docs/ResourceGroupApi.md#create_resource_group) | **POST** /resourceGroup | Creates a new Resource Group.
*ResourceGroupApi* | [**delete_resource_group**](docs/ResourceGroupApi.md#delete_resource_group) | **DELETE** /resourceGroup/{id} | Deletes a Resource Group.
*ResourceGroupApi* | [**get_all_resource_groups**](docs/ResourceGroupApi.md#get_all_resource_groups) | **GET** /resourceGroup | Returns all Resource Groups.
*ResourceGroupApi* | [**get_resource_group_by_id**](docs/ResourceGroupApi.md#get_resource_group_by_id) | **GET** /resourceGroup/{id} | Returns a Resource Group.
*ResourceGroupApi* | [**update_resource_group**](docs/ResourceGroupApi.md#update_resource_group) | **PATCH** /resourceGroup/{id} | Updates a ResourceGroup.
*RuntimeApi* | [**download_file_from_instance**](docs/RuntimeApi.md#download_file_from_instance) | **GET** /runtime/{id}/file | Downloads a file from a VDU.
*RuntimeApi* | [**execute_on_instance**](docs/RuntimeApi.md#execute_on_instance) | **PUT** /runtime/{id}/action/execute | Executes given command on the given VDU.
*RuntimeApi* | [**start_instance**](docs/RuntimeApi.md#start_instance) | **PUT** /runtime/{id}/action/start | Starts the given VDU.
*RuntimeApi* | [**stop_instance**](docs/RuntimeApi.md#stop_instance) | **PUT** /runtime/{id}/action/stop | Stops the given VDU.
*RuntimeApi* | [**upload_file_to_instance_by_file**](docs/RuntimeApi.md#upload_file_to_instance_by_file) | **POST** /runtime/{id}/file | Uploads a file to a VDU.
*RuntimeApi* | [**upload_file_to_instance_by_path**](docs/RuntimeApi.md#upload_file_to_instance_by_path) | **POST** /runtime/{id}/path | Uploads a file to a VDU.
*TOSCAApi* | [**deploy_tosca_template**](docs/TOSCAApi.md#deploy_tosca_template) | **POST** /tosca | Deploys a Tosca template.
*VDUApi* | [**delete_vdu**](docs/VDUApi.md#delete_vdu) | **DELETE** /vdu/{id} | Terminates a VDU.
*VDUApi* | [**deploy_vdu**](docs/VDUApi.md#deploy_vdu) | **POST** /vdu | Allocates resources in the target cloud.
*VDUApi* | [**get_all_vdus**](docs/VDUApi.md#get_all_vdus) | **GET** /vdu | Returns all VDUs.
*VDUApi* | [**get_vdu_by_id**](docs/VDUApi.md#get_vdu_by_id) | **GET** /vdu/{id} | Returns a VDU.
*VDUApi* | [**update_vdu**](docs/VDUApi.md#update_vdu) | **PATCH** /vdu/{id} | Updates a VDU.


## Documentation For Models

 - [CommandExecutionBody](docs/CommandExecutionBody.md)
 - [Event](docs/Event.md)
 - [FileDownloadBody](docs/FileDownloadBody.md)
 - [FileUploadBody](docs/FileUploadBody.md)
 - [KeyValuePair](docs/KeyValuePair.md)
 - [Network](docs/Network.md)
 - [PoP](docs/PoP.md)
 - [ResourceGroup](docs/ResourceGroup.md)
 - [VDU](docs/VDU.md)


## Documentation For Authorization

 All endpoints do not require authorization.


# Source
Source code for other ElasTest projects can be found in the [GitHub ElasTest
Group].

# News
Follow us on Twitter @[ElasTest Twitter].

# Contribution policy
You can contribute to the ElasTest community through bug-reports, bug-fixes,
new code or new documentation. For contributing to the ElasTest community,
you can use the issue support of GitHub providing full information about your
contribution and its value. In your contributions, you must comply with the
following guidelines

* You must specify the specific contents of your contribution either through a
  detailed bug description, through a pull-request or through a patch.
* You must specify the licensing restrictions of the code you contribute.
* For newly created code to be incorporated in the ElasTest code-base, you
  must accept ElasTest to own the code copyright, so that its open source
  nature is guaranteed.
* You must justify appropriately the need and value of your contribution. The
  ElasTest project has no obligations in relation to accepting contributions
  from third parties.
* The ElasTest project leaders have the right of asking for further
  explanations, tests or validations of any code contributed to the community
  before it being incorporated into the ElasTest code-base. You must be ready
  to addressing all these kind of concerns before having your code approved.

# Licensing and distribution
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


[Apache 2.0 License]: http://www.apache.org/licenses/LICENSE-2.0
[ElasTest]: http://elastest.io/
[ElasTest Logo]: http://elastest.io/images/logos_elastest/elastest-logo-gray-small.png
[ElasTest Twitter]: https://twitter.com/elastestio
[GitHub ElasTest Group]: https://github.com/elastest
[Bugtracker]: https://github.com/elastest/bugtracker



