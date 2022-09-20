# togai_client.MetricsApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **POST** /metrics | Get togai metrics.


# **get_metrics**
> GetMetricsResponse get_metrics()

Get togai metrics.

To get the metrics, you make a POST request to the /metrics resource. You can query up to five metrics in a single request. Single response dataset can contain a maximum of 100 data points.

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import metrics_api
from togai_client.model.get_metrics_request import GetMetricsRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.get_metrics_response import GetMetricsResponse
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
    api_instance = metrics_api.MetricsApi(api_client)
    get_metrics_request = GetMetricsRequest(
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        metric_queries=[
            MetricQuery(
                id="id_example",
                name=MetricName("EVENTS"),
                aggregation_period="DAY",
                group_by="group_by_example",
                filters=[
                    MetricQueryFilterEntry(
                        field_name="field_name_example",
                        field_values=[
                            "field_values_example",
                        ],
                    ),
                ],
            ),
        ],
    ) # GetMetricsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get togai metrics.
        api_response = api_instance.get_metrics(get_metrics_request=get_metrics_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metrics_request** | [**GetMetricsRequest**](GetMetricsRequest.md)|  | [optional]

### Return type

[**GetMetricsResponse**](GetMetricsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request. Please check the response message for failure details. |  -  |
**401** | Credential is not valid. Please check the response message for failure details. |  -  |
**403** | Credential does not have access to get metrics. |  -  |
**429** | Request throttled. Please check the response message on the failure details. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

