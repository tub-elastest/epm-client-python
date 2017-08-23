# swagger_client.VDUApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vdu**](VDUApi.md#delete_vdu) | **DELETE** /vdu/{id} | Terminates a VDU.
[**deploy_vdu**](VDUApi.md#deploy_vdu) | **POST** /vdu | Allocates resources in the target cloud.
[**get_all_vdus**](VDUApi.md#get_all_vdus) | **GET** /vdu | Returns all VDUs.
[**get_vdu_by_id**](VDUApi.md#get_vdu_by_id) | **GET** /vdu/{id} | Returns a VDU.
[**update_vdu**](VDUApi.md#update_vdu) | **PATCH** /vdu/{id} | Updates a VDU.


# **delete_vdu**
> str delete_vdu(id)

Terminates a VDU.

Terminates the VDU that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VDUApi()
id = 'id_example' # str | ID of VDU

try: 
    # Terminates a VDU.
    api_response = api_instance.delete_vdu(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VDUApi->delete_vdu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_vdu**
> VDU deploy_vdu(body)

Allocates resources in the target cloud.

Allocates resources defined as a VDU in the cloud to be deployed in the target cloud environment. It instantiates computing resources, deploys artifacts on them and manages the their lifecycle

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VDUApi()
body = swagger_client.VDU() # VDU | Defintion of a VDU which defines resources that have to be deployed

try: 
    # Allocates resources in the target cloud.
    api_response = api_instance.deploy_vdu(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VDUApi->deploy_vdu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VDU**](VDU.md)| Defintion of a VDU which defines resources that have to be deployed | 

### Return type

[**VDU**](VDU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vdus**
> list[VDU] get_all_vdus()

Returns all VDUs.

Returns all VDUs with all its details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VDUApi()

try: 
    # Returns all VDUs.
    api_response = api_instance.get_all_vdus()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VDUApi->get_all_vdus: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VDU]**](VDU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vdu_by_id**
> VDU get_vdu_by_id(id)

Returns a VDU.

Returns the VDU with the given ID. Returns all its details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VDUApi()
id = 'id_example' # str | ID of VDU

try: 
    # Returns a VDU.
    api_response = api_instance.get_vdu_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VDUApi->get_vdu_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 

### Return type

[**VDU**](VDU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vdu**
> VDU update_vdu(id, body)

Updates a VDU.

Updates an already deployed VDU.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VDUApi()
id = 'id_example' # str | ID of VDU
body = swagger_client.VDU() # VDU | VDU object that needs to be updated.

try: 
    # Updates a VDU.
    api_response = api_instance.update_vdu(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VDUApi->update_vdu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 
 **body** | [**VDU**](VDU.md)| VDU object that needs to be updated. | 

### Return type

[**VDU**](VDU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

