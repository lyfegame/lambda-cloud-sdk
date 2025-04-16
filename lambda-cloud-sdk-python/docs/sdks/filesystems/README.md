# Filesystems
(*filesystems*)

## Overview

### Available Operations

* [list_filesystems](#list_filesystems) - List filesystems
* [create_filesystem](#create_filesystem) - Create filesystem
* [filesystem_delete](#filesystem_delete) - Delete filesystem

## list_filesystems

Retrieves a list of your filesystems.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.filesystems.list_filesystems(security=lambda_cloud_sdk.ListFilesystemsSecurity(
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
| `security`                                                          | [models.ListFilesystemsSecurity](../../listfilesystemssecurity.md)  | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFilesystemsResponseBody](../../models/listfilesystemsresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.ListFilesystemsFilesystemsResponseBody         | 401                                                   | application/json                                      |
| models.ListFilesystemsFilesystemsResponseResponseBody | 403                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## create_filesystem

Creates a new filesystem.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.filesystems.create_filesystem(security=lambda_cloud_sdk.CreateFilesystemSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), name="[\"my-filesytem\"]", region=lambda_cloud_sdk.PublicRegionCode.US_SOUTH_3)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.CreateFilesystemSecurity](../../models/createfilesystemsecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | The name of the filesystem.                                                 | [<br/>"my-filesytem"<br/>]                                                  |
| `region`                                                                    | [models.PublicRegionCode](../../models/publicregioncode.md)                 | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.CreateFilesystemResponseBody](../../models/createfilesystemresponsebody.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.CreateFilesystemFilesystemsResponse400ResponseBody | 400                                                       | application/json                                          |
| models.CreateFilesystemFilesystemsResponseBody            | 401                                                       | application/json                                          |
| models.CreateFilesystemFilesystemsResponseResponseBody    | 403                                                       | application/json                                          |
| models.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## filesystem_delete

Deletes the filesystem with the specified ID. The filesystem must not be attached to any running instances at the time of deletion.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.filesystems.filesystem_delete(security=lambda_cloud_sdk.FilesystemDeleteSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `security`                                                                  | [models.FilesystemDeleteSecurity](../../models/filesystemdeletesecurity.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.FilesystemDeleteResponseBody](../../models/filesystemdeleteresponsebody.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.FilesystemDeleteFilesystemsResponse400ResponseBody | 400                                                       | application/json                                          |
| models.FilesystemDeleteFilesystemsResponseBody            | 401                                                       | application/json                                          |
| models.FilesystemDeleteFilesystemsResponseResponseBody    | 403                                                       | application/json                                          |
| models.FilesystemDeleteFilesystemsResponse404ResponseBody | 404                                                       | application/json                                          |
| models.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |