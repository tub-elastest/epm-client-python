# epm_client.ClusterApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_worker**](ClusterApi.md#add_worker) | **GET** /cluster/{id}/add/{machineId} | Adds a worker to the cluster.
[**create_cluster**](ClusterApi.md#create_cluster) | **POST** /cluster/create | Creates a new cluster.
[**delete_cluster**](ClusterApi.md#delete_cluster) | **DELETE** /cluster/{id} | Deletes a Cluster.
[**get_all_clusters**](ClusterApi.md#get_all_clusters) | **GET** /cluster | Returns all clusters
[**set_up_cluster**](ClusterApi.md#set_up_cluster) | **GET** /cluster/{id}/{type} | Sets up the specified cluster to install the specified technology and connected it.


# **add_worker**
> str add_worker(id, machine_id)

Adds a worker to the cluster.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ClusterApi()
id = 'id_example' # str | ID of Cluster
machine_id = 'machine_id_example' # str | The ID of either a Worker or a VDU, which will be added to the cluster

try: 
    # Adds a worker to the cluster.
    api_response = api_instance.add_worker(id, machine_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->add_worker: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Cluster | 
 **machine_id** | **str**| The ID of either a Worker or a VDU, which will be added to the cluster | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster**
> Cluster create_cluster(cluster_from_resource_group)

Creates a new cluster.

Receives an Identifier for a ResourceGroup and an array of types to setup the Resource Group as a cluster.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ClusterApi()
cluster_from_resource_group = epm_client.ClusterFromResourceGroup() # ClusterFromResourceGroup | Body to create Cluster from ResourceGroup

try: 
    # Creates a new cluster.
    api_response = api_instance.create_cluster(cluster_from_resource_group)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->create_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_from_resource_group** | [**ClusterFromResourceGroup**](ClusterFromResourceGroup.md)| Body to create Cluster from ResourceGroup | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> str delete_cluster(id)

Deletes a Cluster.

Deletes the Cluster that matches with a given ID.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ClusterApi()
id = 'id_example' # str | ID of Cluster

try: 
    # Deletes a Cluster.
    api_response = api_instance.delete_cluster(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->delete_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Cluster | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_clusters**
> list[Cluster] get_all_clusters()

Returns all clusters

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ClusterApi()

try: 
    # Returns all clusters
    api_response = api_instance.get_all_clusters()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_all_clusters: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Cluster]**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_up_cluster**
> str set_up_cluster(id, type)

Sets up the specified cluster to install the specified technology and connected it.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.ClusterApi()
id = 'id_example' # str | ID of Cluster
type = 'type_example' # str | type of technology

try: 
    # Sets up the specified cluster to install the specified technology and connected it.
    api_response = api_instance.set_up_cluster(id, type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->set_up_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Cluster | 
 **type** | **str**| type of technology | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

