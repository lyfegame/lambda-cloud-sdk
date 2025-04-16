# Firewalls
(*firewalls*)

## Overview

### Available Operations

* [firewall_rules_list](#firewall_rules_list) - List inbound firewall rules
* [firewall_rules_set](#firewall_rules_set) - Replace inbound firewall rules

## firewall_rules_list

Retrieves a list of your firewall rules.

**Note:** Firewall rules do not apply to the **us-south-1** region.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.firewalls.firewall_rules_list(security=lambda_cloud_sdk.FirewallRulesListSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `security`                                                             | [models.FirewallRulesListSecurity](../../firewallruleslistsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.FirewallRulesListResponseBody](../../models/firewallruleslistresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.FirewallRulesListFirewallsResponseBody         | 401                                                   | application/json                                      |
| models.FirewallRulesListFirewallsResponseResponseBody | 403                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## firewall_rules_set

Overwrites the inbound firewall rules currently active for your account's instances with the desired rules.

**Note:** Firewall rules do not apply to the **us-south-1** region.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.firewalls.firewall_rules_set(security=lambda_cloud_sdk.FirewallRulesSetSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), data=[

    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.FirewallRulesSetSecurity](../../models/firewallrulessetsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `data`                                                                      | List[[models.FirewallRule](../../models/firewallrule.md)]                   | :heavy_check_mark:                                                          | The list of inbound firewall rules.                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.FirewallRulesSetResponseBody](../../models/firewallrulessetresponsebody.md)**

### Errors

| Error Type                                           | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| models.FirewallRulesSetFirewallsResponseBody         | 401                                                  | application/json                                     |
| models.FirewallRulesSetFirewallsResponseResponseBody | 403                                                  | application/json                                     |
| models.APIError                                      | 4XX, 5XX                                             | \*/\*                                                |