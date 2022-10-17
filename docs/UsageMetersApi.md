# togai_client.UsageMetersApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_usage_meter**](UsageMetersApi.md#activate_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name}/activate | Activate usage meter
[**create_usage_meter**](UsageMetersApi.md#create_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters | Create an usage meter
[**deactivate_usage_meter**](UsageMetersApi.md#deactivate_usage_meter) | **POST** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name}/deactivate | Deactivate usage meter
[**delete_usage_meter**](UsageMetersApi.md#delete_usage_meter) | **DELETE** /usage_meter/{usage_meter_name} | Delete an Usage Meter
[**get_usage_meter**](UsageMetersApi.md#get_usage_meter) | **GET** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name} | Get usage meter
[**get_usage_meters_for_event_schema**](UsageMetersApi.md#get_usage_meters_for_event_schema) | **GET** /event_schema/{event_schema_name}/usage_meters | List usage meters for event schema
[**update_usage_meter**](UsageMetersApi.md#update_usage_meter) | **PATCH** /event_schema/{event_schema_name}/usage_meters/{usage_meter_name} | Update an usage meter


# **activate_usage_meter**
> UsageMeter activate_usage_meter(event_schema_name, usage_meter_name)

Activate usage meter

Activate usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.usage_meter import UsageMeter
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    usage_meter_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Activate usage meter
        api_response = api_instance.activate_usage_meter(event_schema_name, usage_meter_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->activate_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **usage_meter_name** | **str**|  |

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_usage_meter**
> UsageMeter create_usage_meter(event_schema_name, create_usage_meter_request)

Create an usage meter

Create an usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.usage_meter import UsageMeter
from togai_client.model.create_usage_meter_request import CreateUsageMeterRequest
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    create_usage_meter_request = CreateUsageMeterRequest(
        name='''HBXK5yBV3g
8ZVqP4n2BNC''',
        description="description_example",
        type="COUNTER",
        aggregation="DRAFT",
        computations=[
            Computation(
                id="id_example",
                matcher='''{
  "and": [
    {"in": [{"var": "dimension.city"}, "chennai", "mumbai"]},
    "or": [
      {">": [{"var": "attribute.distance"}, 100]},
      {"<": [{"var": "attribute.distance"}, 20]}
    ]
  ]
}
''',
                computation="{"*":[{"var":"attributes.distance"},0.4]}",
            ),
        ],
    ) # CreateUsageMeterRequest | Payload to create usage meter

    # example passing only required values which don't have defaults set
    try:
        # Create an usage meter
        api_response = api_instance.create_usage_meter(event_schema_name, create_usage_meter_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->create_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **create_usage_meter_request** | [**CreateUsageMeterRequest**](CreateUsageMeterRequest.md)| Payload to create usage meter |

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_usage_meter**
> UsageMeter deactivate_usage_meter(event_schema_name, usage_meter_name)

Deactivate usage meter

Deactivate usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.usage_meter import UsageMeter
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    usage_meter_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deactivate usage meter
        api_response = api_instance.deactivate_usage_meter(event_schema_name, usage_meter_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->deactivate_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **usage_meter_name** | **str**|  |

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_meter**
> BaseSuccessResponse delete_usage_meter(usage_meter_name)

Delete an Usage Meter

Delete an Usage Meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    usage_meter_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an Usage Meter
        api_response = api_instance.delete_usage_meter(usage_meter_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->delete_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_meter_name** | **str**|  |

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

# **get_usage_meter**
> UsageMeter get_usage_meter(event_schema_name, usage_meter_name)

Get usage meter

Get usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.usage_meter import UsageMeter
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    usage_meter_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get usage meter
        api_response = api_instance.get_usage_meter(event_schema_name, usage_meter_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->get_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **usage_meter_name** | **str**|  |

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_meters_for_event_schema**
> UsageMeterPaginatedResponse get_usage_meters_for_event_schema(event_schema_name)

List usage meters for event schema

List usage meters for event schema with pagination and sort

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.usage_meter_paginated_response import UsageMeterPaginatedResponse
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    statuses = "statuses_example" # str | Filter by provided statuses (optional)
    aggregations = "aggregations_example" # str | Filter by provided aggregations (optional)
    next_token = "eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==" # str |  (optional)
    page_size = "10" # str |  (optional)
    sort_order = "ASC" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List usage meters for event schema
        api_response = api_instance.get_usage_meters_for_event_schema(event_schema_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->get_usage_meters_for_event_schema: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List usage meters for event schema
        api_response = api_instance.get_usage_meters_for_event_schema(event_schema_name, statuses=statuses, aggregations=aggregations, next_token=next_token, page_size=page_size, sort_order=sort_order)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->get_usage_meters_for_event_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **statuses** | **str**| Filter by provided statuses | [optional]
 **aggregations** | **str**| Filter by provided aggregations | [optional]
 **next_token** | **str**|  | [optional]
 **page_size** | **str**|  | [optional]
 **sort_order** | **str**|  | [optional]

### Return type

[**UsageMeterPaginatedResponse**](UsageMeterPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list usage_meters request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_meter**
> UsageMeter update_usage_meter(event_schema_name, usage_meter_name, update_usage_meter_request)

Update an usage meter

Update an usage meter

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import usage_meters_api
from togai_client.model.usage_meter import UsageMeter
from togai_client.model.update_usage_meter_request import UpdateUsageMeterRequest
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
    api_instance = usage_meters_api.UsageMetersApi(api_client)
    event_schema_name =  # str | 
    usage_meter_name =  # str | 
    update_usage_meter_request = UpdateUsageMeterRequest(
        description="description_example",
        type="COUNTER",
        aggregation="COUNT",
        computations=[
            Computation(
                id="id_example",
                matcher='''{
  "and": [
    {"in": [{"var": "dimension.city"}, "chennai", "mumbai"]},
    "or": [
      {">": [{"var": "attribute.distance"}, 100]},
      {"<": [{"var": "attribute.distance"}, 20]}
    ]
  ]
}
''',
                computation="{"*":[{"var":"attributes.distance"},0.4]}",
            ),
        ],
    ) # UpdateUsageMeterRequest | Payload to create usage meter

    # example passing only required values which don't have defaults set
    try:
        # Update an usage meter
        api_response = api_instance.update_usage_meter(event_schema_name, usage_meter_name, update_usage_meter_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling UsageMetersApi->update_usage_meter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_schema_name** | **str**|  |
 **usage_meter_name** | **str**|  |
 **update_usage_meter_request** | [**UpdateUsageMeterRequest**](UpdateUsageMeterRequest.md)| Payload to create usage meter |

### Return type

[**UsageMeter**](UsageMeter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get usage event requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

