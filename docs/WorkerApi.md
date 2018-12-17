# epm_client.WorkerApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkerApi.md#create_worker) | **POST** /workers/create | Creates a new worker.
[**delete_worker**](WorkerApi.md#delete_worker) | **DELETE** /workers/{id} | Deletes a Worker.
[**get_all_workers**](WorkerApi.md#get_all_workers) | **GET** /workers | Returns all registered workers
[**install_adapter**](WorkerApi.md#install_adapter) | **GET** /workers/{id}/{type} | Sets up the specified worker to install the specified type of adapter.
[**register_worker**](WorkerApi.md#register_worker) | **POST** /workers | Registers the worker and saves the information.


# **create_worker**
> Worker create_worker(worker_from_vdu)

Creates a new worker.

Receives a package that can be used for creating a new worker.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.WorkerApi()
worker_from_vdu = epm_client.WorkerFromVDU() # WorkerFromVDU | Body to create Worker from VDU

try: 
    # Creates a new worker.
    api_response = api_instance.create_worker(worker_from_vdu)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkerApi->create_worker: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker_from_vdu** | [**WorkerFromVDU**](WorkerFromVDU.md)| Body to create Worker from VDU | 

### Return type

[**Worker**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_worker**
> str delete_worker(id)

Deletes a Worker.

Deletes the Worker that matches with a given ID.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.WorkerApi()
id = 'id_example' # str | ID of Worker

try: 
    # Deletes a Worker.
    api_response = api_instance.delete_worker(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkerApi->delete_worker: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Worker | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_workers**
> list[Worker] get_all_workers()

Returns all registered workers

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.WorkerApi()

try: 
    # Returns all registered workers
    api_response = api_instance.get_all_workers()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkerApi->get_all_workers: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Worker]**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_adapter**
> str install_adapter(id, type)

Sets up the specified worker to install the specified type of adapter.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.WorkerApi()
id = 'id_example' # str | ID of Worker
type = 'type_example' # str | type of adapter

try: 
    # Sets up the specified worker to install the specified type of adapter.
    api_response = api_instance.install_adapter(id, type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkerApi->install_adapter: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Worker | 
 **type** | **str**| type of adapter | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_worker**
> Worker register_worker(body)

Registers the worker and saves the information.

This registers a worker with the information provided.

### Example 
```python
import time
import epm_client
from epm_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = epm_client.WorkerApi()
body = epm_client.Worker() # Worker | worker in a json

try: 
    # Registers the worker and saves the information.
    api_response = api_instance.register_worker(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WorkerApi->register_worker: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Worker**](Worker.md)| worker in a json | 

### Return type

[**Worker**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

