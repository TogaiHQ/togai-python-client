# togai_client.EventIngestionApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest**](EventIngestionApi.md#ingest) | **POST** /ingest | Ingest events to Togai
[**ingest_batch**](EventIngestionApi.md#ingest_batch) | **POST** /ingestBatch | Ingest events to Togai in batch


# **ingest**
> ingest(ingest_event_request)

Ingest events to Togai

API to ingest your application event to Togai for billing and usage analytics. To know the limits on the ingestion api, check our docs - https://togai.com/docs/limits.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import event_ingestion_api
from togai_client.model.ingest_event_request import IngestEventRequest
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
    api_instance = event_ingestion_api.EventIngestionApi(api_client)
    ingest_event_request = IngestEventRequest(
        event=Event(
            event_name="event_name_example",
            id="id_example",
            event_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            account_id="account_id_example",
            event_attributes=[
                EventAttribute(
                    attribute_name="apiUsage",
                    attribute_value="attribute_value_example",
                    attribute_value_unit="attribute_value_unit_example",
                ),
            ],
            dimensions=Dimensions(
                key="key_example",
            ),
        ),
    ) # IngestEventRequest | Request body to ingest events to Togai usage and billing management service.

    # example passing only required values which don't have defaults set
    try:
        # Ingest events to Togai
        api_instance.ingest(ingest_event_request)
    except togai_client.ApiException as e:
        print("Exception when calling EventIngestionApi->ingest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_event_request** | [**IngestEventRequest**](IngestEventRequest.md)| Request body to ingest events to Togai usage and billing management service. |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully accepted to process all the events from payload. |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential \&quot;x-api-key\&quot; is not valid. Please check the response message for failure details. |  -  |
**422** | Unable to process the events as the size of the event payload is above the supported limit. Please check our docs for the api limits - https://togai.com/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**503** | Service is currently unavailable to process the request. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_batch**
> IngestBatchEventResponse ingest_batch(ingest_batch_event_request)

Ingest events to Togai in batch

API to ingest your application event in batch to Togai for billing and usage analytics. To know the limits on the ingestion api, check our docs - https://togai.com/docs/limits.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import event_ingestion_api
from togai_client.model.ingest_batch_event_response import IngestBatchEventResponse
from togai_client.model.error_response import ErrorResponse
from togai_client.model.ingest_batch_event_request import IngestBatchEventRequest
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
    api_instance = event_ingestion_api.EventIngestionApi(api_client)
    ingest_batch_event_request = IngestBatchEventRequest(
        events=[
            Event(
                event_name="event_name_example",
                id="id_example",
                event_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_id="account_id_example",
                event_attributes=[
                    EventAttribute(
                        attribute_name="apiUsage",
                        attribute_value="attribute_value_example",
                        attribute_value_unit="attribute_value_unit_example",
                    ),
                ],
                dimensions=Dimensions(
                    key="key_example",
                ),
            ),
        ],
    ) # IngestBatchEventRequest | Request body to ingest events in batch to Togai usage and billing management service.

    # example passing only required values which don't have defaults set
    try:
        # Ingest events to Togai in batch
        api_response = api_instance.ingest_batch(ingest_batch_event_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling EventIngestionApi->ingest_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_batch_event_request** | [**IngestBatchEventRequest**](IngestBatchEventRequest.md)| Request body to ingest events in batch to Togai usage and billing management service. |

### Return type

[**IngestBatchEventResponse**](IngestBatchEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully accepted to process all the events from payload. |  -  |
**207** | Partial failure. Few events from request were not accepted |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential \&quot;x-api-key\&quot; is not valid. Please check the response message for failure details. |  -  |
**422** | Unable to process the events as the size of the event payload is above the supported limit. Please check our docs for the api limits - https://togai.com/docs/limits. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**503** | Service is currently unavailable to process the request. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

