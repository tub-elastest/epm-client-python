# swagger_client.PoPApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_po_ps**](PoPApi.md#get_all_po_ps) | **GET** /pop | Returns all PoPs.
[**get_po_p_by_id**](PoPApi.md#get_po_p_by_id) | **GET** /pop/{id} | Returns a PoP.
[**register_po_p**](PoPApi.md#register_po_p) | **POST** /pop | Registers a new PoP
[**unregister_po_p**](PoPApi.md#unregister_po_p) | **DELETE** /pop/{id} | Unregisters a PoP.
[**update_po_p**](PoPApi.md#update_po_p) | **PATCH** /pop/{id} | Updates a PoP.


# **get_all_po_ps**
> list[PoP] get_all_po_ps()

Returns all PoPs.

Returns all PoPs with all its details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoPApi()

try: 
    # Returns all PoPs.
    api_response = api_instance.get_all_po_ps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoPApi->get_all_po_ps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PoP]**](PoP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_po_p_by_id**
> PoP get_po_p_by_id(id)

Returns a PoP.

Returns the PoP with the given ID. Returns all its details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoPApi()
id = 'id_example' # str | ID of PoP

try: 
    # Returns a PoP.
    api_response = api_instance.get_po_p_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoPApi->get_po_p_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of PoP | 

### Return type

[**PoP**](PoP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_po_p**
> PoP register_po_p(body)

Registers a new PoP

Registers a new Point-of-Presence represented by a PoP

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoPApi()
body = swagger_client.PoP() # PoP | Defintion of a PoP which defines a Point-of-Presence used to host resources

try: 
    # Registers a new PoP
    api_response = api_instance.register_po_p(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoPApi->register_po_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoP**](PoP.md)| Defintion of a PoP which defines a Point-of-Presence used to host resources | 

### Return type

[**PoP**](PoP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_po_p**
> str unregister_po_p(id)

Unregisters a PoP.

Unregisters the PoP that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoPApi()
id = 'id_example' # str | ID of PoP

try: 
    # Unregisters a PoP.
    api_response = api_instance.unregister_po_p(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoPApi->unregister_po_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of PoP | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_po_p**
> PoP update_po_p(id, body)

Updates a PoP.

Updates an already registered PoP.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoPApi()
id = 'id_example' # str | ID of PoP
body = swagger_client.PoP() # PoP | PoP object that needs to be updated.

try: 
    # Updates a PoP.
    api_response = api_instance.update_po_p(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoPApi->update_po_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of PoP | 
 **body** | [**PoP**](PoP.md)| PoP object that needs to be updated. | 

### Return type

[**PoP**](PoP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

