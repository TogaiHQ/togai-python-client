import datetime
from pprint import pprint
import random

import togai_client
from togai_client.api.event_schemas_api import EventSchemasApi
from togai_client.api.usage_meters_api import UsageMetersApi
from togai_client.api.price_plans_api import PricePlansApi
from togai_client.api.customers_api import CustomersApi
from togai_client.api.accounts_api import AccountsApi
from togai_client.api.event_ingestion_api import EventIngestionApi
from togai_client.api.metrics_api import MetricsApi

from togai_client.model.create_event_schema_request import CreateEventSchemaRequest
from togai_client.model.dimensions_schema import DimensionsSchema
from togai_client.model.event import Event
from togai_client.model.event_attribute import EventAttribute
from togai_client.model.event_attribute_schema import EventAttributeSchema
from togai_client.model.metric_name import MetricName
from togai_client.model.pricing_cycle import PricingCycle
from togai_client.model.rate_card import RateCard
from togai_client.model.pricing_cycle_start_offset import PricingCycleStartOffset
from togai_client.model.associate_price_plan_request import AssociatePricePlanRequest
from togai_client.model.create_customer_request import CreateCustomerRequest
from togai_client.model.create_price_plan_request import CreatePricePlanRequest
from togai_client.model.create_usage_meter_request import CreateUsageMeterRequest
from togai_client.model.ingest_event_request import IngestEventRequest
from togai_client.model.get_metrics_request import GetMetricsRequest
from togai_client.model.rate_card_usage import RateCardUsage
from togai_client.model.rate_card_usage_value import RateCardUsageValue
from togai_client.model.usage_strategy import UsageStrategy
from togai_client.model.metric_query import MetricQuery
from togai_client.model.metric_query_filter_entry import MetricQueryFilterEntry


API_TOKEN = "YOUR_API_TOKEN"
BASE_PATH = "https://sandbox-api.togai.com"

configuration = togai_client.Configuration(
    host=BASE_PATH,
    access_token=API_TOKEN
)

api_client = togai_client.ApiClient(configuration=configuration)

# Following example simulates the pricing of an API based SMS service which charges their customers based on region and size of the message.
# Follow the steps below to create the required entities in Togai, and then ingest an event.

# Step 1: Create an Event Schema to define the event structure, attributes (can be usage value) and dimensions (can be used filters in usage meters i.e country in this case)
event_schema_api = EventSchemasApi(api_client=api_client)
create_event_schema_request = CreateEventSchemaRequest(
    name="message_sent",
    attributes=[
        EventAttributeSchema(
            name="sms_id"
        )
    ],
    dimensions=[
        DimensionsSchema(
            name="country"
        )
    ]
)
event_schema = event_schema_api.create_event_schema(create_event_schema_request=create_event_schema_request)
pprint(event_schema)

# Step 2: Activate the Event Schema
event_schema_api.activate_event_schema(event_schema_name=event_schema.name)

# Step 3: Create a Usage Meter to meter the usage with aggregation methods
usage_meters_api = UsageMetersApi(api_client=api_client)
create_usage_meter_request = CreateUsageMeterRequest(
    name="message_count",
    type="COUNTER",
    aggregation="COUNT",
    computations=[
            {
                # The matcher are written in Json Logic format
                "matcher": '''{
                    "==": [
                        {
                            "var": "dimensions.country"
                        },
                        "US"
                    ]
                }''',
                "computation": "1"
            }
        ]
)
usage_meter = usage_meters_api.create_usage_meter(event_schema_name=event_schema.name, create_usage_meter_request=create_usage_meter_request)
pprint(usage_meter)

# Step 4: Activate a usage meter
usage_meters_api.activate_usage_meter(event_schema_name=event_schema.name, usage_meter_name=usage_meter.name)

# Step 5: Create a Price plan to convert the usage into a billable price
create_price_plan_request = CreatePricePlanRequest(
    name="price-plan",
    pricing_cycle=PricingCycle(
        interval="MONTHLY",
        start_type="STATIC",
        start_offset= PricingCycleStartOffset(
            day_offset="1",
            month_offset="NIL"
        ),
        grace_period=1
    ),
    rate_card=RateCard(
        type="USAGE",
        usage_config=RateCardUsage(**{
                usage_meter.name: RateCardUsageValue(
                    name="SMS charges",
                    rate_strategy="PER_UNIT",
                    slab_strategy="TIER",
                    slabs=[
                        UsageStrategy(
                            rate=0.2,
                            start_after=0.0,
                            order=1
                        ),
                        UsageStrategy(
                            rate=0.1,
                            start_after=10000.0,
                            order=2
                        )
                    ]
                )
            }
        )
    ),
)
price_plan_api = PricePlansApi(api_client=api_client)
price_plan = price_plan_api.create_price_plan(create_price_plan_request=create_price_plan_request)
pprint(price_plan)

# Step 6: Activate the Price Plan
price_plan_api.activate_price_plan(price_plan_name=price_plan.name)

# Step 7: Create customers to associate price plans
create_customer_request = CreateCustomerRequest(
    name="customer1",
    id="1",
    primary_email="email@togai.com",
    billing_address="221B Baker Street, Marylebone, London NW1 6XE, United Kingdom"
)
customers_api = CustomersApi(api_client=api_client)
customer = customers_api.create_customer(create_customer_request=create_customer_request)
pprint(customer)

# Step 8: Associate the customer/account to the price plan
associate_price_plan_request = AssociatePricePlanRequest(
    price_plan_name=price_plan.name,
    effective_from=datetime.date.today()
)
associate_price_plan_api = AccountsApi(api_client=api_client)
associate_price_plan = associate_price_plan_api.associate_price_plan(customer_id=customer.id, account_id=customer.id, associate_price_plan_request=associate_price_plan_request)
pprint(associate_price_plan)

# Step 9: Ingest events
events_api = EventIngestionApi(api_client=api_client)
event_request = IngestEventRequest(
    event=Event(
        id="random-string" + str(random.random()),
        event_name=event_schema.name,
        event_timestamp=datetime.datetime.utcnow(),
        account_id=customer.id,
        event_attributes=[
            EventAttribute(
                attribute_name="sms_id",
                attribute_value="random-string" + str(random.random())
            )
        ],
        dimensions={
            "country": "US"
        }
    )
)
event = events_api.ingest(ingest_event_request=event_request)
pprint(event)

# Step 10: Get the usage metrics 
now = datetime.datetime.utcnow()
yesterday = datetime.datetime.utcnow() - datetime.timedelta(days=1)
metrics_api = MetricsApi(api_client=api_client)
usage_metrics_request = GetMetricsRequest(
    start_time=yesterday,
    end_time=now,
    metric_queries=[
        MetricQuery(
            id="usage-metrics",
            name=MetricName("USAGE"),
            aggregation_period="DAY"
        )
    ]
)
usage_metrics = metrics_api.get_metrics(get_metrics_request=usage_metrics_request)
pprint(usage_metrics)


# Step 11: Get the revenue metrics
# Revenue metrics might take a bit of time to be reflected in the system
# You can check the docs on the amount of time it takes for events to get processed for revenue.
revenue_metrics_request = GetMetricsRequest(
    start_time=yesterday,
    end_time=now,
    metric_queries=[
        MetricQuery(
            id="revenue-metrics",
            name=MetricName("REVENUE"),
            aggregation_period="DAY"
        )
    ]
)
revenue_metrics = metrics_api.get_metrics(get_metrics_request=revenue_metrics_request)
pprint(revenue_metrics)

# Revenue metrics for a specific customer
customer_revenue_metrics_request = GetMetricsRequest(
    start_time=yesterday,
    end_time=now,
    metric_queries=[
        MetricQuery(
            id="customer-revenue-metrics",
            name=MetricName("REVENUE"),
            aggregation_period="DAY",
            filters=[
                MetricQueryFilterEntry(
                    field_name="CUSTOMER_ID",
                    field_values=[customer.id]
                )
            ]
        )
    ]
)
customer_revenue_metrics = metrics_api.get_metrics(get_metrics_request=customer_revenue_metrics_request)
pprint(customer_revenue_metrics)








