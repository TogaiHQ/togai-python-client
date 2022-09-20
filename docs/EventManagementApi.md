# togai_client.EventManagementApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventManagementApi.md#get_events) | **GET** /events | Get usage events from Togai
[**get_single_event**](EventManagementApi.md#get_single_event) | **GET** /events/{event_id} | Get the usage event given event id.


# **get_events**
> GetEventsResponse get_events()

Get usage events from Togai

API to get usage events ingested to Togai.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import event_management_api
from togai_client.model.get_events_response import GetEventsResponse
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
    api_instance = event_management_api.EventManagementApi(api_client)
    next_token = "eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==" # str | Pagination token used as a marker to get records from next page. (optional)
    status = "PROCESSED" # str | Filter option to filter the events by processed/unprocessed status. (optional)
    account_id = "1234" # str | Filter option to filter the events based on account id. (optional)
    page_size = 10 # int | Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. (optional)
    start_time = 1650110402000 # int | Start time filter in epoch milli seconds (optional)
    end_time = 1650110402000 # int | End time filter in epoch milli seconds (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage events from Togai
        api_response = api_instance.get_events(next_token=next_token, status=status, account_id=account_id, page_size=page_size, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventManagementApi->get_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_token** | **str**| Pagination token used as a marker to get records from next page. | [optional]
 **status** | **str**| Filter option to filter the events by processed/unprocessed status. | [optional]
 **account_id** | **str**| Filter option to filter the events based on account id. | [optional]
 **page_size** | **int**| Maximum page size expected by client to return the record list.    NOTE: Max page size cannot be more than 50. Also 50 is the default page size if no value is provided. | [optional]
 **start_time** | **int**| Start time filter in epoch milli seconds | [optional]
 **end_time** | **int**| End time filter in epoch milli seconds | [optional]

### Return type

[**GetEventsResponse**](GetEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to list events. |  -  |
**422** | Unable to process the query parameters provided. Please check our docs for the api limits - https://togai.io/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_event**
> GetEventResponse get_single_event(event_id)

Get the usage event given event id.

API to get the event given the event id.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import event_management_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.get_event_response import GetEventResponse
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
    api_instance = event_management_api.EventManagementApi(api_client)
    event_id =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the usage event given event id.
        api_response = api_instance.get_single_event(event_id)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventManagementApi->get_single_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  |

### Return type

[**GetEventResponse**](GetEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to get events. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

