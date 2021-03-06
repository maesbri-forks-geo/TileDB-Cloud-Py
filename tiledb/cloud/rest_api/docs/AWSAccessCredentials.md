# AWSAccessCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_access_key** | **str** | aws secret access key, never returned in get requests | [optional] 
**access_key_id** | **str** | aws access key | [optional] 
**service_role_arn** | **str** | aws service role to use for access | [optional] 
**name** | **str** | human readable name | [optional] 
**default** | **bool** | true if this is the default credential to be used within this namespace | [optional] 
**buckets** | **list[str]** | a whitelist of one or more buckets this key should access | [optional] 
**created_at** | **datetime** | Time when udf dependencies was created (rfc3339) | [optional] 
**updated_at** | **datetime** | Time when udf dependencies was last updated (rfc3339) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


