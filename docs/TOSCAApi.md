# epm_client.TOSCAApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_tosca_template**](TOSCAApi.md#deploy_tosca_template) | **POST** /tosca | Deploys a Tosca template.


# **deploy_tosca_template**
> ResourceGroup deploy_tosca_template(body)

Deploys a Tosca template.

The TOSCA template defines VDUs, Networks and the PoPs where to allocate the virtual resources

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.TOSCAApi()
body = epm_client.ResourceGroup() # ResourceGroup | TOSCA formatted template

try: 
    # Deploys a Tosca template.
    api_response = api_instance.deploy_tosca_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TOSCAApi->deploy_tosca_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroup**](ResourceGroup.md)| TOSCA formatted template | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

