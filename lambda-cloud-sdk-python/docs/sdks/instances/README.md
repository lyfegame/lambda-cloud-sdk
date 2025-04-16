# Instances
(*instances*)

## Overview

### Available Operations

* [list_instances](#list_instances) - List running instances
* [get_instance](#get_instance) - Retrieve instance details
* [post_instance](#post_instance) - Update instance details
* [list_instance_types](#list_instance_types) - List available instance types
* [launch_instance](#launch_instance) - Launch instances
* [restart_instance](#restart_instance) - Restart instances
* [terminate_instance](#terminate_instance) - Terminate instances

## list_instances

Retrieves a list of your running instances.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ListInstancesSecurity](../../listinstancessecurity.md)      | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListInstancesResponseBody](../../models/listinstancesresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.ListInstancesInstancesResponseBody         | 401                                               | application/json                                  |
| models.ListInstancesInstancesResponseResponseBody | 403                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## get_instance

Retrieves the details of a specific instance, including whether or not the instance is running.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.get_instance(security=lambda_cloud_sdk.GetInstanceSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), id="0920582c7ff041399e34823a0be62549")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.GetInstanceSecurity](../../models/getinstancesecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier (ID) of the instance                          | 0920582c7ff041399e34823a0be62549                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetInstanceResponseBody](../../models/getinstanceresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.GetInstanceInstancesResponseBody            | 401                                                | application/json                                   |
| models.GetInstanceInstancesResponseResponseBody    | 403                                                | application/json                                   |
| models.GetInstanceInstancesResponse404ResponseBody | 404                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## post_instance

Updates the details of the specified instance.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.post_instance(security=lambda_cloud_sdk.PostInstanceSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), id="0920582c7ff041399e34823a0be62549", name="My Instance")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.PostInstanceSecurity](../../models/postinstancesecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier (ID) of the instance                          | 0920582c7ff041399e34823a0be62549                                    |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The new, user-provided name for the instance.                       | My Instance                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PostInstanceResponseBody](../../models/postinstanceresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.PostInstanceInstancesResponse400ResponseBody | 400                                                 | application/json                                    |
| models.PostInstanceInstancesResponseBody            | 401                                                 | application/json                                    |
| models.PostInstanceInstancesResponseResponseBody    | 403                                                 | application/json                                    |
| models.PostInstanceInstancesResponse404ResponseBody | 404                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## list_instance_types

Retrieves a list of the instance types currently offered on Lambda's public cloud, as well as details about each type. Details include resource specifications, pricing, and regional availability.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.list_instance_types(security=lambda_cloud_sdk.ListInstanceTypesSecurity(
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
| `security`                                                             | [models.ListInstanceTypesSecurity](../../listinstancetypessecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.ListInstanceTypesResponseBody](../../models/listinstancetypesresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.ListInstanceTypesInstancesResponseBody         | 401                                                   | application/json                                      |
| models.ListInstanceTypesInstancesResponseResponseBody | 403                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## launch_instance

Launches a Lambda On-Demand Cloud instance.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.launch_instance(security=lambda_cloud_sdk.LaunchInstanceSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), region_name=lambda_cloud_sdk.PublicRegionCode.US_WEST_3, instance_type_name="gpu_8x_a100", ssh_key_names=[
        "my-public-key",
    ], file_system_names=[

    ], name="My Instance")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                                                   | [models.LaunchInstanceSecurity](../../models/launchinstancesecurity.md)                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                              |
| `region_name`                                                                                                                                                                                                                                                                                | [models.PublicRegionCode](../../models/publicregioncode.md)                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                           | N/A                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                              |
| `instance_type_name`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                           | The type of instance you want to launch. To retrieve a list of available instance types, see<br/>[List available instance types](#get-/api/v1/instance-types).                                                                                                                               | gpu_8x_a100                                                                                                                                                                                                                                                                                  |
| `ssh_key_names`                                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                           | The names of the SSH keys you want to use to provide access to the instance.<br/>Currently, exactly one SSH key must be specified.                                                                                                                                                           | [<br/>"my-public-key"<br/>]                                                                                                                                                                                                                                                                  |
| `file_system_names`                                                                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | The names of the filesystems you want to attach to the instance.<br/>Currently, you can attach only one filesystem during instance creation.<br/>By default, no filesystems are attached.                                                                                                    | [<br/>"my-filesystem"<br/>]                                                                                                                                                                                                                                                                  |
| `name`                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | The name you want to assign to your instance. Must be 64 characters or fewer.                                                                                                                                                                                                                | My Instance                                                                                                                                                                                                                                                                                  |
| `image`                                                                                                                                                                                                                                                                                      | [Optional[models.InstanceLaunchRequestImage]](../../models/instancelaunchrequestimage.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | The machine image you want to use. Defaults to the latest Lambda Stack image.                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                              |
| `user_data`                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | An instance configuration string specified in a valid<br/>[cloud-init user-data](https://cloudinit.readthedocs.io/en/latest/explanation/format.html)<br/>format. You can use this field to configure your instance on launch. The<br/>user data string must be plain text and cannot exceed 1MB in size. |                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                              |

### Response

**[models.LaunchInstanceResponseBody](../../models/launchinstanceresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.LaunchInstanceInstancesResponse400ResponseBody | 400                                                   | application/json                                      |
| models.LaunchInstanceInstancesResponseBody            | 401                                                   | application/json                                      |
| models.LaunchInstanceInstancesResponseResponseBody    | 403                                                   | application/json                                      |
| models.LaunchInstanceInstancesResponse404ResponseBody | 404                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## restart_instance

Restarts one or more instances.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.restart_instance(security=lambda_cloud_sdk.RestartInstanceSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), instance_ids=[
        "0920582c7ff041399e34823a0be62549",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.RestartInstanceSecurity](../../models/restartinstancesecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `instance_ids`                                                            | List[*str*]                                                               | :heavy_check_mark:                                                        | The unique identifiers (IDs) of the instances to restart.                 | [<br/>"0920582c7ff041399e34823a0be62549"<br/>]                            |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.RestartInstanceResponseBody](../../models/restartinstanceresponsebody.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.RestartInstanceInstancesResponseBody            | 401                                                    | application/json                                       |
| models.RestartInstanceInstancesResponseResponseBody    | 403                                                    | application/json                                       |
| models.RestartInstanceInstancesResponse404ResponseBody | 404                                                    | application/json                                       |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## terminate_instance

Terminates one or more instances.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.terminate_instance(security=lambda_cloud_sdk.TerminateInstanceSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), instance_ids=[
        "0920582c7ff041399e34823a0be62549",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.TerminateInstanceSecurity](../../models/terminateinstancesecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |                                                                               |
| `instance_ids`                                                                | List[*str*]                                                                   | :heavy_check_mark:                                                            | The unique identifiers (IDs) of the instances to terminate.                   | [<br/>"0920582c7ff041399e34823a0be62549"<br/>]                                |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.TerminateInstanceResponseBody](../../models/terminateinstanceresponsebody.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.TerminateInstanceInstancesResponseBody            | 401                                                      | application/json                                         |
| models.TerminateInstanceInstancesResponseResponseBody    | 403                                                      | application/json                                         |
| models.TerminateInstanceInstancesResponse404ResponseBody | 404                                                      | application/json                                         |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |