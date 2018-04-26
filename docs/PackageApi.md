# epm_client.PackageApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_package**](PackageApi.md#delete_package) | **DELETE** /packages/{id} | Deletes a package.
[**receive_package**](PackageApi.md#receive_package) | **POST** /packages | Receives a package.


# **delete_package**
> delete_package(id)

Deletes a package.

Deletes the package that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.PackageApi()
id = 'id_example' # str | ID of Package

try: 
    # Deletes a package.
    api_instance.delete_package(id)
except ApiException as e:
    print("Exception when calling PackageApi->delete_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Package | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_package**
> ResourceGroup receive_package(file)

Receives a package.

Receives a package so that it can be forwarded to the correct environment.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.PackageApi()
file = '/path/to/file.txt' # file | Package in a multipart form

try: 
    # Receives a package.
    api_response = api_instance.receive_package(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageApi->receive_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Package in a multipart form | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

