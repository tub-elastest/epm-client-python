# epm_client.KeyApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_key**](KeyApi.md#add_key) | **POST** /keys | Uploads a key to the EPM.
[**delete_key**](KeyApi.md#delete_key) | **DELETE** /keys/{id} | Deletes a Key.
[**get_all_keys**](KeyApi.md#get_all_keys) | **GET** /keys | Returns all available Keys


# **add_key**
> Key add_key(body)

Uploads a key to the EPM.

This uploads a key to the EPM, so it can be later used when registering workers.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.KeyApi()
body = epm_client.Key() # Key | Key in a json

try: 
    # Uploads a key to the EPM.
    api_response = api_instance.add_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyApi->add_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Key**](Key.md)| Key in a json | 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> str delete_key(id)

Deletes a Key.

Deletes the Key that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.KeyApi()
id = 'id_example' # str | ID of Key

try: 
    # Deletes a Key.
    api_response = api_instance.delete_key(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyApi->delete_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Key | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_keys**
> list[Key] get_all_keys()

Returns all available Keys

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.KeyApi()

try: 
    # Returns all available Keys
    api_response = api_instance.get_all_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyApi->get_all_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Key]**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

