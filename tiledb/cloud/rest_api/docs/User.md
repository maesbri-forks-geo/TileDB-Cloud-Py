# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique id of user | [optional] 
**username** | **str** | username must be unique | 
**password** | **str** | password | [optional] 
**name** | **str** | the user&#39;s full, real name | [optional] 
**email** | **str** | the user&#39;s email | [optional] 
**is_valid_email** | **bool** | user&#39;s email is validated to be correct | [optional] 
**stripe_connect** | **bool** | Denotes that the user is able to apply pricing to arrays by means of Stripe Connect | [optional] 
**company** | **str** | the user&#39;s company | [optional] 
**logo** | **str** | the user&#39;s logo | [optional] 
**last_activity_date** | **datetime** | when the user last logged in (set by the server) | [optional] 
**timezone** | **str** |  | [optional] 
**organizations** | [**list[OrganizationUser]**](OrganizationUser.md) | Array of organizations a user is part of and their roles | [optional] 
**allowed_actions** | [**list[NamespaceActions]**](NamespaceActions.md) | list of actions user is allowed to do on this organization | [optional] 
**enabled_features** | **list[str]** | List of extra/optional/beta features to enable for namespace | [optional] 
**unpaid_subscription** | **bool** | A notice that the user has an unpaid subscription | [optional] 
**notebook_settings** | [**NotebookSettings**](NotebookSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


