# rest_api.NotebookApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notebook_server_status**](NotebookApi.md#get_notebook_server_status) | **GET** /notebooks/server/{namespace}/status | 
[**shutdown_notebook_server**](NotebookApi.md#shutdown_notebook_server) | **DELETE** /notebooks/server/{namespace} | 


# **get_notebook_server_status**
> NotebookStatus get_notebook_server_status(namespace)



Get status of the notebook server

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
api_instance = rest_api.NotebookApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace notebook is in (an organization name or user's username)

try:
    api_response = api_instance.get_notebook_server_status(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotebookApi->get_notebook_server_status: %s\n" % e)
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
api_instance = rest_api.NotebookApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace notebook is in (an organization name or user's username)

try:
    api_response = api_instance.get_notebook_server_status(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotebookApi->get_notebook_server_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace notebook is in (an organization name or user&#39;s username) | 

### Return type

[**NotebookStatus**](NotebookStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of running notebook |  -  |
**202** | Notebook server is pending |  -  |
**404** | Notebook is not running |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_notebook_server**
> shutdown_notebook_server(namespace)



Shutdown a notebook server

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
api_instance = rest_api.NotebookApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace notebook is in (an organization name or user's username)

try:
    api_instance.shutdown_notebook_server(namespace)
except ApiException as e:
    print("Exception when calling NotebookApi->shutdown_notebook_server: %s\n" % e)
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
api_instance = rest_api.NotebookApi(rest_api.ApiClient(configuration))
namespace = 'namespace_example' # str | namespace notebook is in (an organization name or user's username)

try:
    api_instance.shutdown_notebook_server(namespace)
except ApiException as e:
    print("Exception when calling NotebookApi->shutdown_notebook_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| namespace notebook is in (an organization name or user&#39;s username) | 

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
**204** | Notebook shutdown successfully |  -  |
**404** | Notebook is not running |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

