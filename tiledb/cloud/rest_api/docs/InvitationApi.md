# rest_api.InvitationApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](InvitationApi.md#accept_invitation) | **POST** /invitations/{invitation} | 
[**cancel_join_organization**](InvitationApi.md#cancel_join_organization) | **DELETE** /invitations/{invitation}/{organization}/join | 
[**cancel_share_array_by_invite**](InvitationApi.md#cancel_share_array_by_invite) | **DELETE** /invitations/{invitation}/{namespace}/{array}/share | 
[**fetch_invitations**](InvitationApi.md#fetch_invitations) | **GET** /invitations | 
[**join_organization**](InvitationApi.md#join_organization) | **POST** /invitations/{organization}/join | 
[**share_array_by_invite**](InvitationApi.md#share_array_by_invite) | **POST** /invitations/{namespace}/{array}/share | 


# **accept_invitation**
> accept_invitation(invitation)



Accepts invitation

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
invitation = 'invitation_example' # str | the id of invitation about to be accepted

try:
    api_instance.accept_invitation(invitation)
except ApiException as e:
    print("Exception when calling InvitationApi->accept_invitation: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
invitation = 'invitation_example' # str | the id of invitation about to be accepted

try:
    api_instance.accept_invitation(invitation)
except ApiException as e:
    print("Exception when calling InvitationApi->accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | **str**| the id of invitation about to be accepted | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Invitation was accepted successfully |  -  |
**404** | Could not find invitation identifier |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_join_organization**
> cancel_join_organization(invitation, organization)



Cancels join organization invitation

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
invitation = 'invitation_example' # str | the id of invitation about to be cancelled
organization = 'organization_example' # str | name or uuid of organization

try:
    api_instance.cancel_join_organization(invitation, organization)
except ApiException as e:
    print("Exception when calling InvitationApi->cancel_join_organization: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
invitation = 'invitation_example' # str | the id of invitation about to be cancelled
organization = 'organization_example' # str | name or uuid of organization

try:
    api_instance.cancel_join_organization(invitation, organization)
except ApiException as e:
    print("Exception when calling InvitationApi->cancel_join_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | **str**| the id of invitation about to be cancelled | 
 **organization** | **str**| name or uuid of organization | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Invitation cancelled successfully |  -  |
**404** | No invitation was found to cancel |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_share_array_by_invite**
> cancel_share_array_by_invite(namespace, invitation, array)



Cancels array sharing invitation

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace array is in (an organization name or user's username)
invitation = 'invitation_example' # str | the id of invitation about to be cancelled
array = 'array_example' # str | name/uri of array that is url-encoded

try:
    api_instance.cancel_share_array_by_invite(namespace, invitation, array)
except ApiException as e:
    print("Exception when calling InvitationApi->cancel_share_array_by_invite: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace array is in (an organization name or user's username)
invitation = 'invitation_example' # str | the id of invitation about to be cancelled
array = 'array_example' # str | name/uri of array that is url-encoded

try:
    api_instance.cancel_share_array_by_invite(namespace, invitation, array)
except ApiException as e:
    print("Exception when calling InvitationApi->cancel_share_array_by_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace array is in (an organization name or user&#39;s username) | 
 **invitation** | **str**| the id of invitation about to be cancelled | 
 **array** | **str**| name/uri of array that is url-encoded | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Invitation cancelled successfully |  -  |
**404** | No invitation was found to cancel |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_invitations**
> InvitationData fetch_invitations(organization=organization, array=array, start=start, end=end, page=page, per_page=per_page, type=type, status=status, orderby=orderby)



Fetch a list of invitations

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
organization = 'organization_example' # str | name or id of organization to filter (optional)
array = 'array_example' # str | name/uri of array that is url-encoded to filter (optional)
start = 56 # int | start time for tasks to filter by (optional)
end = 56 # int | end time for tasks to filter by (optional)
page = 56 # int | pagination offset (optional)
per_page = 56 # int | pagination limit (optional)
type = 'type_example' # str | invitation type, \"ARRAY_SHARE\", \"JOIN_ORGANIZATION\" (optional)
status = 'status_example' # str | Filter to only return \"PENDING\", \"ACCEPTED\" (optional)
orderby = 'orderby_example' # str | sort by which field valid values include timestamp, array_name, organization_name (optional)

try:
    api_response = api_instance.fetch_invitations(organization=organization, array=array, start=start, end=end, page=page, per_page=per_page, type=type, status=status, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->fetch_invitations: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
organization = 'organization_example' # str | name or id of organization to filter (optional)
array = 'array_example' # str | name/uri of array that is url-encoded to filter (optional)
start = 56 # int | start time for tasks to filter by (optional)
end = 56 # int | end time for tasks to filter by (optional)
page = 56 # int | pagination offset (optional)
per_page = 56 # int | pagination limit (optional)
type = 'type_example' # str | invitation type, \"ARRAY_SHARE\", \"JOIN_ORGANIZATION\" (optional)
status = 'status_example' # str | Filter to only return \"PENDING\", \"ACCEPTED\" (optional)
orderby = 'orderby_example' # str | sort by which field valid values include timestamp, array_name, organization_name (optional)

try:
    api_response = api_instance.fetch_invitations(organization=organization, array=array, start=start, end=end, page=page, per_page=per_page, type=type, status=status, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationApi->fetch_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| name or id of organization to filter | [optional] 
 **array** | **str**| name/uri of array that is url-encoded to filter | [optional] 
 **start** | **int**| start time for tasks to filter by | [optional] 
 **end** | **int**| end time for tasks to filter by | [optional] 
 **page** | **int**| pagination offset | [optional] 
 **per_page** | **int**| pagination limit | [optional] 
 **type** | **str**| invitation type, \&quot;ARRAY_SHARE\&quot;, \&quot;JOIN_ORGANIZATION\&quot; | [optional] 
 **status** | **str**| Filter to only return \&quot;PENDING\&quot;, \&quot;ACCEPTED\&quot; | [optional] 
 **orderby** | **str**| sort by which field valid values include timestamp, array_name, organization_name | [optional] 

### Return type

[**InvitationData**](InvitationData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of invitations and pagination metadata |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_organization**
> join_organization(organization, email_invite)



Sends email to multiple recipients with joining information regarding an organization

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
organization = 'organization_example' # str | name or uuid of organization
email_invite = rest_api.InvitationOrganizationJoinEmail() # InvitationOrganizationJoinEmail | list of email recipients

try:
    api_instance.join_organization(organization, email_invite)
except ApiException as e:
    print("Exception when calling InvitationApi->join_organization: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
organization = 'organization_example' # str | name or uuid of organization
email_invite = rest_api.InvitationOrganizationJoinEmail() # InvitationOrganizationJoinEmail | list of email recipients

try:
    api_instance.join_organization(organization, email_invite)
except ApiException as e:
    print("Exception when calling InvitationApi->join_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| name or uuid of organization | 
 **email_invite** | [**InvitationOrganizationJoinEmail**](InvitationOrganizationJoinEmail.md)| list of email recipients | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Email sent successfully to user for email confirmation link |  -  |
**404** | Could not reach one or more recipients |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_array_by_invite**
> share_array_by_invite(namespace, array, email_invite)



Sends email to multiple recipients with sharing information regarding an array

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace array is in (an organization name or user's username)
array = 'array_example' # str | name/uri of array that is url-encoded
email_invite = rest_api.InvitationArrayShareEmail() # InvitationArrayShareEmail | list of email recipients

try:
    api_instance.share_array_by_invite(namespace, array, email_invite)
except ApiException as e:
    print("Exception when calling InvitationApi->share_array_by_invite: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import rest_api
from rest_api.rest import ApiException
from pprint import pprint
configuration = rest_api.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-TILEDB-REST-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TILEDB-REST-API-KEY'] = 'Bearer'
configuration = rest_api.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/v1
configuration.host = "http://localhost/v1"
# Create an instance of the API class
api_instance = rest_api.InvitationApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace array is in (an organization name or user's username)
array = 'array_example' # str | name/uri of array that is url-encoded
email_invite = rest_api.InvitationArrayShareEmail() # InvitationArrayShareEmail | list of email recipients

try:
    api_instance.share_array_by_invite(namespace, array, email_invite)
except ApiException as e:
    print("Exception when calling InvitationApi->share_array_by_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace array is in (an organization name or user&#39;s username) | 
 **array** | **str**| name/uri of array that is url-encoded | 
 **email_invite** | [**InvitationArrayShareEmail**](InvitationArrayShareEmail.md)| list of email recipients | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Email sent successfully to user for email confirmation link |  -  |
**404** | Could not reach one or more recipients |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

