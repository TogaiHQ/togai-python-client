# togai_client.AccountsApi

All URIs are relative to *https://sandbox-api.togai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_aliases**](AccountsApi.md#add_aliases) | **POST** /customers/{customer_id}/accounts/{account_id}/add_aliases | Add Aliases to account
[**associate_price_plan**](AccountsApi.md#associate_price_plan) | **POST** /customers/{customer_id}/accounts/{account_id}/price_plans | Associate a plan to an account
[**create_account**](AccountsApi.md#create_account) | **POST** /customers/{customer_id}/accounts | Create an account
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /customers/{customer_id}/accounts/{account_id} | Delete an account
[**get_account**](AccountsApi.md#get_account) | **GET** /customers/{customer_id}/accounts/{account_id} | Get an account
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /customers/{customer_id}/accounts | List accounts of customer
[**remove_aliases**](AccountsApi.md#remove_aliases) | **POST** /customers/{customer_id}/accounts/{account_id}/remove_aliases | Remove Aliases to account
[**update_account**](AccountsApi.md#update_account) | **PATCH** /customers/{customer_id}/accounts/{account_id} | Update an account


# **add_aliases**
> Account add_aliases(customer_id, account_id, add_account_aliases_request)

Add Aliases to account

Add Aliases to an account by id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.add_account_aliases_request import AddAccountAliasesRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.account import Account
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 
    add_account_aliases_request = AddAccountAliasesRequest(
        aliases=[
            "aliases_example",
        ],
    ) # AddAccountAliasesRequest | Payload to add aliases to account

    # example passing only required values which don't have defaults set
    try:
        # Add Aliases to account
        api_response = api_instance.add_aliases(customer_id, account_id, add_account_aliases_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->add_aliases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |
 **add_account_aliases_request** | [**AddAccountAliasesRequest**](AddAccountAliasesRequest.md)| Payload to add aliases to account |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_price_plan**
> AssociatePricePlanResponse associate_price_plan(customer_id, account_id, associate_price_plan_request)

Associate a plan to an account

Associate a plan to an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.associate_price_plan_request import AssociatePricePlanRequest
from togai_client.model.associate_price_plan_response import AssociatePricePlanResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 
    associate_price_plan_request = AssociatePricePlanRequest(
        price_plan_name="price_plan_name_example",
        effective_from=dateutil_parser('1970-01-01').date(),
        effective_until=dateutil_parser('1970-01-01').date(),
        rate_card_override=RateCard(
            type="USAGE",
            usage_config=RateCardUsage(
                key=RateCardUsageValue(
                    name="name_example",
                    rate_strategy="FLAT",
                    slab_strategy="TIER",
                    slabs=[
                        UsageStrategy(
                            rate=3.14,
                            start_after=3.14,
                            order=1,
                        ),
                    ],
                ),
            ),
            bundle_config=RateCardBundle(
                rate_strategy="FLAT",
                slab_strategy="TIER",
                bundles=[
                    BundleStrategy(
                        name="name_example",
                        rate=3.14,
                        order=1,
                        usage_meters={
                            "key": BundleStrategyUsageMetersValue(
                                start_after=3.14,
                            ),
                        },
                    ),
                ],
            ),
        ),
    ) # AssociatePricePlanRequest | Payload to associate a price plan to an account

    # example passing only required values which don't have defaults set
    try:
        # Associate a plan to an account
        api_response = api_instance.associate_price_plan(customer_id, account_id, associate_price_plan_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->associate_price_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |
 **associate_price_plan_request** | [**AssociatePricePlanRequest**](AssociatePricePlanRequest.md)| Payload to associate a price plan to an account |

### Return type

[**AssociatePricePlanResponse**](AssociatePricePlanResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for associate price plan request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> Account create_account(customer_id, create_account_request)

Create an account

Create an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.create_account_request import CreateAccountRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.account import Account
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    create_account_request = CreateAccountRequest(
        id="id_example",
        name="name_example",
        aliases=[
            "aliases_example",
        ],
    ) # CreateAccountRequest | Payload to create account

    # example passing only required values which don't have defaults set
    try:
        # Create an account
        api_response = api_instance.create_account(customer_id, create_account_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)| Payload to create account |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> BaseSuccessResponse delete_account(customer_id, account_id)

Delete an account

Delete an account by id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an account
        api_response = api_instance.delete_account(customer_id, account_id)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |

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

# **get_account**
> Account get_account(customer_id, account_id)

Get an account

Get an account

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.account import Account
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an account
        api_response = api_instance.get_account(customer_id, account_id)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountPaginatedResponse get_accounts(customer_id)

List accounts of customer

List accounts with pagination and sort

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.account_paginated_response import AccountPaginatedResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    next_token = "eyJsYXN0SXRlbUlkIjogInN0cmluZyIsICJwYWdlU2l6ZSI6IDEyMywgInNvcnRPcmRlciI6ICJhc2MifQ==" # str |  (optional)
    page_size = "10" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts of customer
        api_response = api_instance.get_accounts(customer_id)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts of customer
        api_response = api_instance.get_accounts(customer_id, next_token=next_token, page_size=page_size)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **next_token** | **str**|  | [optional]
 **page_size** | **str**|  | [optional]

### Return type

[**AccountPaginatedResponse**](AccountPaginatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for list customers request |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_aliases**
> Account remove_aliases(customer_id, account_id, remove_account_aliases_request)

Remove Aliases to account

Remove Aliases to an account by id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.error_response import ErrorResponse
from togai_client.model.remove_account_aliases_request import RemoveAccountAliasesRequest
from togai_client.model.account import Account
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 
    remove_account_aliases_request = RemoveAccountAliasesRequest(
        aliases=[
            "aliases_example",
        ],
    ) # RemoveAccountAliasesRequest | Payload to remove aliases from account

    # example passing only required values which don't have defaults set
    try:
        # Remove Aliases to account
        api_response = api_instance.remove_aliases(customer_id, account_id, remove_account_aliases_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->remove_aliases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |
 **remove_account_aliases_request** | [**RemoveAccountAliasesRequest**](RemoveAccountAliasesRequest.md)| Payload to remove aliases from account |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Account update_account(customer_id, account_id, update_account_request)

Update an account

Update an account by id

### Example

* Bearer (Bearer <credential>) Authentication (bearerAuth):

```python
import time
import togai_client
from togai_client.api import accounts_api
from togai_client.model.update_account_request import UpdateAccountRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.account import Account
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
    api_instance = accounts_api.AccountsApi(api_client)
    customer_id =  # str | 
    account_id =  # str | 
    update_account_request = UpdateAccountRequest(
        name="name_example",
    ) # UpdateAccountRequest | Payload to update account

    # example passing only required values which don't have defaults set
    try:
        # Update an account
        api_response = api_instance.update_account(customer_id, account_id, update_account_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **account_id** | **str**|  |
 **update_account_request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| Payload to update account |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response for Create and Get account requests |  -  |
**400** | Error response |  -  |
**401** | Error response |  -  |
**403** | Error response |  -  |
**404** | Error response |  -  |
**429** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

