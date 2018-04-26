# epm_client.AdapterApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_adapters**](AdapterApi.md#get_all_adapters) | **GET** /adapters | Returns all registered adapters


# **get_all_adapters**
> list[Adapter] get_all_adapters()

Returns all registered adapters

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.AdapterApi()

try: 
    # Returns all registered adapters
    api_response = api_instance.get_all_adapters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdapterApi->get_all_adapters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Adapter]**](Adapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

