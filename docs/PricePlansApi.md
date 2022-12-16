# togai_client.PricePlansApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_price_plan**](PricePlansApi.md#activate_price_plan) | **POST** /price_plans/{price_plan_name}/activate | Activate a price plan
[**create_price_plan**](PricePlansApi.md#create_price_plan) | **POST** /price_plans | Create a price plan
[**get_price_plan**](PricePlansApi.md#get_price_plan) | **GET** /price_plans/{price_plan_name} | Get a price plan
[**get_price_plans**](PricePlansApi.md#get_price_plans) | **GET** /price_plans | List price plans
[**update_price_plan**](PricePlansApi.md#update_price_plan) | **PATCH** /price_plans/{price_plan_name} | Update a price plan


# **activate_price_plan**
> PricePlan activate_price_plan(price_plan_name)

Activate a price plan

Activate a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import price_plans_api
from togai_client.model.price_plan import PricePlan
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
    api_instance = price_plans_api.PricePlansApi(api_client)
    price_plan_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Activate a price plan
        api_response = api_instance.activate_price_plan(price_plan_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling PricePlansApi->activate_price_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_name** | **str**|  |

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_plan**
> PricePlan create_price_plan(create_price_plan_request)

Create a price plan

Create a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import price_plans_api
from togai_client.model.create_price_plan_request import CreatePricePlanRequest
from togai_client.model.price_plan import PricePlan
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
    api_instance = price_plans_api.PricePlansApi(api_client)
    create_price_plan_request = CreatePricePlanRequest(
        name="name_example",
        description="description_example",
        price_plan_details=PricePlanDetails(
            pricing_cycle_config=PricingCycleConfig(
                interval="MONTHLY",
                start_type="STATIC",
                start_offset=PricingCycleConfigStartOffset(
                    day_offset="day_offset_example",
                    month_offset="month_offset_example",
                ),
                grace_period=3,
            ),
            rate_cards=[
                RateCard(
                    display_name="display_name_example",
                    pricing_model=PricingModel("TIERED"),
                    rate_config=RateConfigUsage(
                        usage_meter_name="usage_meter_name_example",
                        slabs=[
                            SlabUsage(
                                rate=3.14,
                                start_after=3.14,
                                price_type=PriceType("FLAT"),
                                config={
                                    "key": "key_example",
                                },
                                order=1,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ) # CreatePricePlanRequest | Payload to create price plan

    # example passing only required values which don't have defaults set
    try:
        # Create a price plan
        api_response = api_instance.create_price_plan(create_price_plan_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling PricePlansApi->create_price_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_price_plan_request** | [**CreatePricePlanRequest**](CreatePricePlanRequest.md)| Payload to create price plan |

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plan**
> PricePlan get_price_plan(price_plan_name)

Get a price plan

Get a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import price_plans_api
from togai_client.model.price_plan import PricePlan
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
    api_instance = price_plans_api.PricePlansApi(api_client)
    price_plan_name =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a price plan
        api_response = api_instance.get_price_plan(price_plan_name)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling PricePlansApi->get_price_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_name** | **str**|  |

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_plans**
> PricePlanPaginatedResponse get_price_plans()

List price plans

List price plans with pagination and sort

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import price_plans_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.price_plan_paginated_response import PricePlanPaginatedResponse
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
    api_instance = price_plans_api.PricePlansApi(api_client)
    next_token = "eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==" # str |  (optional)
    page_size = "10" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List price plans
        api_response = api_instance.get_price_plans(next_token=next_token, page_size=page_size)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling PricePlansApi->get_price_plans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**|  | [optional]
 **page_size** | **str**|  | [optional]

### Return type

[**PricePlanPaginatedResponse**](PricePlanPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list price plans request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_plan**
> PricePlan update_price_plan(price_plan_name, update_price_plan_request)

Update a price plan

Update a price plan

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import price_plans_api
from togai_client.model.update_price_plan_request import UpdatePricePlanRequest
from togai_client.model.price_plan import PricePlan
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
    api_instance = price_plans_api.PricePlansApi(api_client)
    price_plan_name =  # str | 
    update_price_plan_request = UpdatePricePlanRequest(
        description="description_example",
        price_plan_details=PricePlanDetailsOverride(
            pricing_cycle_config=PricingCycleConfig(
                interval="MONTHLY",
                start_type="STATIC",
                start_offset=PricingCycleConfigStartOffset(
                    day_offset="day_offset_example",
                    month_offset="month_offset_example",
                ),
                grace_period=3,
            ),
            rate_cards=[
                RateCard(
                    display_name="display_name_example",
                    pricing_model=PricingModel("TIERED"),
                    rate_config=RateConfigUsage(
                        usage_meter_name="usage_meter_name_example",
                        slabs=[
                            SlabUsage(
                                rate=3.14,
                                start_after=3.14,
                                price_type=PriceType("FLAT"),
                                config={
                                    "key": "key_example",
                                },
                                order=1,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ) # UpdatePricePlanRequest | Payload to update price plan

    # example passing only required values which don't have defaults set
    try:
        # Update a price plan
        api_response = api_instance.update_price_plan(price_plan_name, update_price_plan_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling PricePlansApi->update_price_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_plan_name** | **str**|  |
 **update_price_plan_request** | [**UpdatePricePlanRequest**](UpdatePricePlanRequest.md)| Payload to update price plan |

### Return type

[**PricePlan**](PricePlan.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get price plan requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

