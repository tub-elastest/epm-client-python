# swagger_client.RuntimeApi

All URIs are relative to *https://localhost:8180/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file_from_instance**](RuntimeApi.md#download_file_from_instance) | **GET** /runtime/{id}/file | Downloads a file from a VDU.
[**execute_on_instance**](RuntimeApi.md#execute_on_instance) | **PUT** /runtime/{id}/action/execute | Executes given command on the given VDU.
[**start_instance**](RuntimeApi.md#start_instance) | **PUT** /runtime/{id}/action/start | Starts the given VDU.
[**stop_instance**](RuntimeApi.md#stop_instance) | **PUT** /runtime/{id}/action/stop | Stops the given VDU.
[**upload_file_to_instance_by_file**](RuntimeApi.md#upload_file_to_instance_by_file) | **POST** /runtime/{id}/file | Uploads a file to a VDU.
[**upload_file_to_instance_by_path**](RuntimeApi.md#upload_file_to_instance_by_path) | **POST** /runtime/{id}/path | Uploads a file to a VDU.


# **download_file_from_instance**
> file download_file_from_instance(id, file_download_body)

Downloads a file from a VDU.

Download a file with the given filepath from the given VDU.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU
file_download_body = swagger_client.FileDownloadBody() # FileDownloadBody | Contains details of the file to be downloaded from the given Instance

try: 
    # Downloads a file from a VDU.
    api_response = api_instance.download_file_from_instance(id, file_download_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeApi->download_file_from_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 
 **file_download_body** | [**FileDownloadBody**](FileDownloadBody.md)| Contains details of the file to be downloaded from the given Instance | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_on_instance**
> str execute_on_instance(id, command_execution_body)

Executes given command on the given VDU.

Executes the given command on the VDU with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU
command_execution_body = swagger_client.CommandExecutionBody() # CommandExecutionBody | Contains command to be executed and a flag if for the completion of the execution should be awaited

try: 
    # Executes given command on the given VDU.
    api_response = api_instance.execute_on_instance(id, command_execution_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeApi->execute_on_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 
 **command_execution_body** | [**CommandExecutionBody**](CommandExecutionBody.md)| Contains command to be executed and a flag if for the completion of the execution should be awaited | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_instance**
> start_instance(id)

Starts the given VDU.

Starts the VDU with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU

try: 
    # Starts the given VDU.
    api_instance.start_instance(id)
except ApiException as e:
    print("Exception when calling RuntimeApi->start_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_instance**
> stop_instance(id)

Stops the given VDU.

Stops the VDU with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU

try: 
    # Stops the given VDU.
    api_instance.stop_instance(id)
except ApiException as e:
    print("Exception when calling RuntimeApi->stop_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_instance_by_file**
> upload_file_to_instance_by_file(id, remote_path, file)

Uploads a file to a VDU.

Uploads a given file to the given filepath to the given VDU.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU
remote_path = 'remote_path_example' # str | Absolute path where the file should go on the Instance
file = '/path/to/file.txt' # file | File which has to be uploaded to the Instance. Either this or the hostPath but not both can be provided.

try: 
    # Uploads a file to a VDU.
    api_instance.upload_file_to_instance_by_file(id, remote_path, file)
except ApiException as e:
    print("Exception when calling RuntimeApi->upload_file_to_instance_by_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 
 **remote_path** | **str**| Absolute path where the file should go on the Instance | 
 **file** | **file**| File which has to be uploaded to the Instance. Either this or the hostPath but not both can be provided. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_instance_by_path**
> upload_file_to_instance_by_path(id, file_upload_body)

Uploads a file to a VDU.

Uploads a given file from the host path to the given file path to the given VDU.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RuntimeApi()
id = 'id_example' # str | ID of VDU
file_upload_body = swagger_client.FileUploadBody() # FileUploadBody | Contains details of the file with the given path to upload to the Instance

try: 
    # Uploads a file to a VDU.
    api_instance.upload_file_to_instance_by_path(id, file_upload_body)
except ApiException as e:
    print("Exception when calling RuntimeApi->upload_file_to_instance_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of VDU | 
 **file_upload_body** | [**FileUploadBody**](FileUploadBody.md)| Contains details of the file with the given path to upload to the Instance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

