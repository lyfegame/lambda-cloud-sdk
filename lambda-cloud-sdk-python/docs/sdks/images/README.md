# Images
(*images*)

## Overview

### Available Operations

* [list_images](#list_images) - List available images

## list_images

Retrieves a list of available images by region.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.images.list_images(security=lambda_cloud_sdk.ListImagesSecurity(
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
| `security`                                                          | [models.ListImagesSecurity](../../listimagessecurity.md)            | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListImagesResponseBody](../../models/listimagesresponsebody.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.ListImagesImagesResponseBody         | 401                                         | application/json                            |
| models.ListImagesImagesResponseResponseBody | 403                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |