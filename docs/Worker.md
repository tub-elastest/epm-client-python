# Worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**vdu_id** | **str** | The vduId if the worker was created from a vdu. | [optional] 
**epm_ip** | **str** | This is the IP where the EPM is reachable for the Worker. This is needed because the Worker has to be able to reach the EPM for registering adapters. | [optional] 
**type** | **list[str]** | The types which this worker supports at the moment when this information is requested. | [optional] 
**auth_credentials** | [**AuthCredentials**](AuthCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


