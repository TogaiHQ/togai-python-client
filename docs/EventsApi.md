# togai_client.EventsApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_event_schema**](EventsApi.md#activate_event_schema) | **POST** /event_schema/{event_schema_name}/activate | Activate an event schema
[**create_event_schema**](EventsApi.md#create_event_schema) | **POST** /event_schema | Create an event schema
[**deactivate_event_schema**](EventsApi.md#deactivate_event_schema) | **POST** /event_schema/{event_schema_name}/deactivate | Deactivate an event schema
[**delete_event_schema**](EventsApi.md#delete_event_schema) | **DELETE** /event_schema/{event_schema_name} | Delete an event schema
[**get_event_schema**](EventsApi.md#get_event_schema) | **GET** /event_schema/{event_schema_name} | Get an event schema
[**list_event_schema_versions**](EventsApi.md#list_event_schema_versions) | **GET** /event_schema/{event_schema_name}/versions | List all event schema versions
[**list_event_schemas**](EventsApi.md#list_event_schemas) | **GET** /event_schema | List event schemas
[**update_event_schema**](EventsApi.md#update_event_schema) | **PATCH** /event_schema/{event_schema_name} | Update an event schema


# **activate_event_schema**
> EventSchema activate_event_schema(event_schema_name)

Activate an event schema

Activate an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema import EventSchema
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Activate an event schema
        api_response = api_instance.activate_event_schema(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->activate_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_schema**
> EventSchema create_event_schema(create_event_schema_request)

Create an event schema

Create an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema import EventSchema
from togai_client.model.create_event_schema_request import CreateEventSchemaRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    create_event_schema_request = CreateEventSchemaRequest(
        name='''HBXK5yBV3g
8ZVqP4n2BNC''',
        description="description_example",
        attributes=[
            EventAttributeSchema(
                name="distance",
                default_unit="kms",
            ),
        ],
        dimensions=[
            DimensionsSchema(
                name="city",
            ),
        ],
    ) # CreateEventSchemaRequest | Payload to create event schema

    # example passing only required values which don't have defaults set
    try:
        # Create an event schema
        api_response = api_instance.create_event_schema(create_event_schema_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->create_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_schema_request** | [**CreateEventSchemaRequest**](CreateEventSchemaRequest.md)| Payload to create event schema |

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_event_schema**
> EventSchema deactivate_event_schema(event_schema_name)

Deactivate an event schema

Deactivate an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema import EventSchema
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deactivate an event schema
        api_response = api_instance.deactivate_event_schema(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->deactivate_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_schema**
> BaseSuccessResponse delete_event_schema(event_schema_name)

Delete an event schema

Delete an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.base_success_response import BaseSuccessResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an event schema
        api_response = api_instance.delete_event_schema(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->delete_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |

### Return type

[**BaseSuccessResponse**](BaseSuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_schema**
> EventSchema get_event_schema(event_schema_name)

Get an event schema

Get an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema import EventSchema
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 
    version =  # int | Optional version to get a specific version. Gets latest version if it is not provided. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an event schema
        api_response = api_instance.get_event_schema(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->get_event_schema: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an event schema
        api_response = api_instance.get_event_schema(event_schema_name, version=version)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->get_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **version** | **int**| Optional version to get a specific version. Gets latest version if it is not provided. | [optional]

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_schema_versions**
> EventSchemaVersionsResponse list_event_schema_versions(event_schema_name)

List all event schema versions

List all event schema versions

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema_versions_response import EventSchemaVersionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # List all event schema versions
        api_response = api_instance.list_event_schema_versions(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->list_event_schema_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |

### Return type

[**EventSchemaVersionsResponse**](EventSchemaVersionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list event schema versions request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_schemas**
> EventSchemaListPaginatedResponse list_event_schemas()

List event schemas

List event schemas with pagination and sort

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.event_schema_list_paginated_response import EventSchemaListPaginatedResponse
from togai_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    statuses = "statuses_example" # str | Filter by provided statuses (optional)
    next_token = "eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==" # str |  (optional)
    page_size = "10" # str |  (optional)
    sort_order = "ASC" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List event schemas
        api_response = api_instance.list_event_schemas(statuses=statuses, next_token=next_token, page_size=page_size, sort_order=sort_order)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->list_event_schemas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statuses** | **str**| Filter by provided statuses | [optional]
 **next_token** | **str**|  | [optional]
 **page_size** | **str**|  | [optional]
 **sort_order** | **str**|  | [optional]

### Return type

[**EventSchemaListPaginatedResponse**](EventSchemaListPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list events request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_schema**
> EventSchema update_event_schema(event_schema_name, update_event_schema_request)

Update an event schema

Update an event schema

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import events_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.event_schema import EventSchema
from togai_client.model.update_event_schema_request import UpdateEventSchemaRequest
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-api.togai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = togai_client.Configuration(
    host = "https://sandbox-api.togai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Bearer <credential>): bearerAuth
configuration = togai_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with togai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    event_schema_name =  # str | 
    update_event_schema_request = UpdateEventSchemaRequest(
        description="description_example",
        attributes=[
            EventAttributeSchema(
                name="distance",
                default_unit="kms",
            ),
        ],
        dimensions=[
            DimensionsSchema(
                name="city",
            ),
        ],
    ) # UpdateEventSchemaRequest | Payload to update event schema

    # example passing only required values which don't have defaults set
    try:
        # Update an event schema
        api_response = api_instance.update_event_schema(event_schema_name, update_event_schema_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventsApi->update_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **update_event_schema_request** | [**UpdateEventSchemaRequest**](UpdateEventSchemaRequest.md)| Payload to update event schema |

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get event schema requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

