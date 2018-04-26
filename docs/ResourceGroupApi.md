# epm_client.ResourceGroupApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_group**](ResourceGroupApi.md#create_resource_group) | **POST** /resourceGroup | Creates a new Resource Group.
[**delete_resource_group**](ResourceGroupApi.md#delete_resource_group) | **DELETE** /resourceGroup/{id} | Deletes a Resource Group.
[**get_all_resource_groups**](ResourceGroupApi.md#get_all_resource_groups) | **GET** /resourceGroup | Returns all Resource Groups.
[**get_resource_group_by_id**](ResourceGroupApi.md#get_resource_group_by_id) | **GET** /resourceGroup/{id} | Returns a Resource Group.
[**update_resource_group**](ResourceGroupApi.md#update_resource_group) | **PATCH** /resourceGroup/{id} | Updates a ResourceGroup.


# **create_resource_group**
> ResourceGroup create_resource_group(body)

Creates a new Resource Group.

Creates a new Resource Group and allocates the defined resources in the defined PoPs.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ResourceGroupApi()
body = epm_client.ResourceGroup() # ResourceGroup | Defintion of a Resource Group which includes all VDUs, Network and respective PoPs

try: 
    # Creates a new Resource Group.
    api_response = api_instance.create_resource_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceGroupApi->create_resource_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroup**](ResourceGroup.md)| Defintion of a Resource Group which includes all VDUs, Network and respective PoPs | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_group**
> str delete_resource_group(id)

Deletes a Resource Group.

Deletes the Resource Group that matches with a given ID.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ResourceGroupApi()
id = 'id_example' # str | ID of ResourceGroup

try: 
    # Deletes a Resource Group.
    api_response = api_instance.delete_resource_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceGroupApi->delete_resource_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of ResourceGroup | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resource_groups**
> list[ResourceGroup] get_all_resource_groups()

Returns all Resource Groups.

Returns all Resource Groups with all details.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ResourceGroupApi()

try: 
    # Returns all Resource Groups.
    api_response = api_instance.get_all_resource_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceGroupApi->get_all_resource_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ResourceGroup]**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group_by_id**
> ResourceGroup get_resource_group_by_id(id)

Returns a Resource Group.

Returns the Resource Group with the given ID. Returns all its details.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ResourceGroupApi()
id = 'id_example' # str | ID of ResourceGroup

try: 
    # Returns a Resource Group.
    api_response = api_instance.get_resource_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceGroupApi->get_resource_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of ResourceGroup | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_group**
> ResourceGroup update_resource_group(id, body)

Updates a ResourceGroup.

Updates an existing ResourceGroup.

### Example 
```python
from __future__ import print_statement
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ResourceGroupApi()
id = 'id_example' # str | ID of ResourceGroup
body = epm_client.ResourceGroup() # ResourceGroup | ResourceGroup that needs to be updated.

try: 
    # Updates a ResourceGroup.
    api_response = api_instance.update_resource_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceGroupApi->update_resource_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of ResourceGroup | 
 **body** | [**ResourceGroup**](ResourceGroup.md)| ResourceGroup that needs to be updated. | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](../README.md)

