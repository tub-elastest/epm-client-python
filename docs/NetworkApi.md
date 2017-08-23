# swagger_client.NetworkApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network**](NetworkApi.md#create_network) | **POST** /network | Creates a new network.
[**delete_network**](NetworkApi.md#delete_network) | **DELETE** /network/{id} | Deletes a network.
[**get_all_networks**](NetworkApi.md#get_all_networks) | **GET** /network | Returns all existing networks.
[**get_network_by_id**](NetworkApi.md#get_network_by_id) | **GET** /network/{id} | Returns a network.
[**update_network**](NetworkApi.md#update_network) | **PATCH** /network/{id} | Updates a Network.


# **create_network**
> Network create_network(body)

Creates a new network.

Creates a new network in the target cloud environment with the given CIDR.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
body = swagger_client.Network() # Network | Defintion of a Network which has to be created on a certain PoP

try: 
    # Creates a new network.
    api_response = api_instance.create_network(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Network**](Network.md)| Defintion of a Network which has to be created on a certain PoP | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> str delete_network(id)

Deletes a network.

Deletes the network that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | ID of Network

try: 
    # Deletes a network.
    api_response = api_instance.delete_network(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Network | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_networks**
> list[Network] get_all_networks()

Returns all existing networks.

Returns all networks with all details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()

try: 
    # Returns all existing networks.
    api_response = api_instance.get_all_networks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_all_networks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Network]**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_by_id**
> Network get_network_by_id(id)

Returns a network.

Returns the network with the given ID. Returns all its details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | ID of Network

try: 
    # Returns a network.
    api_response = api_instance.get_network_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Network | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network**
> Network update_network(id, body)

Updates a Network.

Updates an existing Network.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()
id = 'id_example' # str | ID of Network
body = swagger_client.Network() # Network | Network that needs to be updated.

try: 
    # Updates a Network.
    api_response = api_instance.update_network(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->update_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Network | 
 **body** | [**Network**](Network.md)| Network that needs to be updated. | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

