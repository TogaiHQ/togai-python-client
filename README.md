# togai-client
![PyPI](https://img.shields.io/pypi/v/togai-client)

[Togai](https://www.togai.com/) is an end to end pricing infrastructure that enable you with metering, aggregating, pricing and billing for your application.

This is an official Typescript client library for using [Togai APIs](https://docs.togai.com/reference).

- API version: 1.0
- Package version: 1.0.2
For more information, please visit [https://docs.togai.com](https://docs.togai.com)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

```sh
pip install togai-client
```
(you may need to run `pip` with root permission: `sudo pip install togai-client`)

Then import the package:
```python
import togai_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import togai_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:
You will need a API_TOKEN to use the API. You can get one from your Togai Account

```python

import time
import togai_client
from pprint import pprint
from togai_client.api import accounts_api
from togai_client.model.account import Account
from togai_client.model.account_paginated_response import AccountPaginatedResponse
from togai_client.model.add_account_aliases_request import AddAccountAliasesRequest
from togai_client.model.associate_price_plan_request import AssociatePricePlanRequest
from togai_client.model.associate_price_plan_response import AssociatePricePlanResponse
from togai_client.model.base_success_response import BaseSuccessResponse
from togai_client.model.create_account_request import CreateAccountRequest
from togai_client.model.error_response import ErrorResponse
from togai_client.model.remove_account_aliases_request import RemoveAccountAliasesRequest
from togai_client.model.update_account_request import UpdateAccountRequest
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

    try:
        # Add Aliases to account
        api_response = api_instance.add_aliases(customer_id, account_id, add_account_aliases_request)
        pprint(api_response)
    except togai_client.ApiException as e:
        print("Exception when calling AccountsApi->add_aliases: %s\n" % e)
```

You can get a detailed step-by-step guide for a sample ingestion and metering at [examples directory](https://github.com/TogaiHQ/togai-python-client/tree/main/examples)
For a more detailed documentation for every api and models, please refer to the [docs directory](https://github.com/TogaiHQ/togai-python-client/tree/main/docs)

## Author

engg@togai.com


