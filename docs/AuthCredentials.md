# AuthCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **str** | The name of the key saved in EPM, which can be used to execute runtime operations on this VDU. | [optional] 
**user** | **str** | This is the user, which the EPM will use when trying to ssh in to the Worker. | 
**passphrase** | **str** | This is the Passphrase of the Key provided for connecting to the Worker. | [optional] 
**password** | **str** | This is the password of the user, which can be left blank if no password is needed. | [optional] 
**port** | **int** | The ssh port of the worker, where the EPM can reach it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


