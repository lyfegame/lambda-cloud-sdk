# lambda-cloud-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *lambda-cloud-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=lambda-cloud-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/fundamental-research-labs/lambda-cloud). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Lambda Cloud API: 
The Lambda Cloud API provides a set of REST API endpoints you can use to create
and manage your Lambda Cloud resources.

# Response types and formats

The format of each response object depends on whether the request succeeded or failed.

### Success responses

When a request succeeds, the API returns a response object in the following format. `<PAYLOAD>`
represents the endpoint-specific data object returned as part of the response object.

```json
{
    "data": <PAYLOAD>
}
```

### Error responses

When a request fails, the API returns an error response object in the following format:

```json
{
    "error": {
        "code": string,
        "message": string,
        "suggestion": string?
    }
}
```

- `code`: A machine- and human-readable error code specific to a particular failure mode.
- `message`: An explanation of the error.
- `suggestion`: When present, a suggestion for how to address the error.

<div style="border: 0.075rem solid #47afe8; border-radius: .2rem; font-size: 13px;
  box-shadow: 0 0.2rem 0.5rem #0000000d,0 0 0.05rem #0000001a; margin-top: 1em;">
  <div style="background-color: #0489D12f; padding: .4rem 2rem .4rem .6rem; font-weight: bold;">Note</div>
  <div style="background-color: transparent; padding: .4rem .6rem; line-height: 1.4;">When
  handling errors, avoid relying on the values of <code>message</code> or <code>suggestion</code>, as
  these values are subject to change. Instead, use the value of <code>code</code>.</div>
</div>

#### Provider errors

In some cases, you might receive errors that come from upstream services/providers rather than directly
from Lambda services. You can identify these errors by their error code prefix, `provider/`.

Common provider errors include:

- Network outages or connectivity issues
- Service unavailability
- Quota limitations or resource exhaustion

An example of a typical service unavailability error:

```json
{
  "error": {
    "code": "provider/internal-unavailable",
    "message": "Provider unavailable",
    "suggestion": "Try again shortly",
  }
}
```

<div class="divider" part="operation-divider"></div>

# Authentication

The Lambda Cloud API uses API keys to authenticate incoming requests. You
can generate a new API key pair or view your existing API keys by visiting
the
<a href="/api-keys" style="color: var(--highlight-primary);
text-decoration: none" target="_blank">API keys page</a> in the Lambda Cloud
dashboard.

In general, Lambda recommends passing an HTTP Bearer header that contains
your API key:

```http
Authorization: Bearer <YOUR-API-KEY>
```

### Authenticating with `curl`

The API also supports passing an HTTP Basic header. This option chiefly exists
to support `curl`'s `-u` flag, which allows you to pass your credentials
without having to write out the full `Authorization: Basic` header string.
For example:

```bash
curl -X GET "https://cloud.lambda.ai/api/v1/instances" \
  -H 'accept: application/json' \
  -u '<YOUR-API-KEY>:'
```

If your use case requires it, you can also pass the HTTP Basic header directly.
The value you pass must be a Base64-encoded string containing your API key
and a trailing colon:

```http
Authorization: Basic <BASE64-ENCODED-API-KEY-WITH-COLON>
```

<div style="border: 0.075rem solid #E48603; border-radius: .2rem; font-size: 13px;
  box-shadow: 0 0.2rem 0.5rem #0000000d,0 0 0.05rem #0000001a; margin-top: 1em;">
  <div style="background-color: #E486031a; padding: .4rem 2rem .4rem .6rem; font-weight: bold;">Important</div>
  <div style="background-color: transparent; padding: .4rem .6rem; line-height: 1.4;">If
  you make a request without including a supported <code>Authorization</code>
  header, the request will fail.</div>
</div>
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [lambda-cloud-sdk](#lambda-cloud-sdk)
* [Response types and formats](#response-types-and-formats)
* [Authentication](#authentication)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from lambda-cloud-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "lambda-cloud-sdk",
# ]
# ///

from lambda_cloud_sdk import LambdaCloudSDK

sdk = LambdaCloudSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK

async def main():

    async with LambdaCloudSDK() as lcs_client:

        res = await lcs_client.instances.list_instances_async(security=lambda_cloud_sdk.ListInstancesSecurity(
            basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
                username="",
                password="",
            ),
        ))

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                      | Type | Scheme     | Environment Variable                                    |
| ------------------------- | ---- | ---------- | ------------------------------------------------------- |
| `username`<br/>`password` | http | HTTP Basic | `LAMBDACLOUDSDK_USERNAME`<br/>`LAMBDACLOUDSDK_PASSWORD` |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:


### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(

    ))

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [filesystems](docs/sdks/filesystems/README.md)

* [list_filesystems](docs/sdks/filesystems/README.md#list_filesystems) - List filesystems
* [create_filesystem](docs/sdks/filesystems/README.md#create_filesystem) - Create filesystem
* [filesystem_delete](docs/sdks/filesystems/README.md#filesystem_delete) - Delete filesystem

### [firewalls](docs/sdks/firewalls/README.md)

* [firewall_rules_list](docs/sdks/firewalls/README.md#firewall_rules_list) - List inbound firewall rules
* [firewall_rules_set](docs/sdks/firewalls/README.md#firewall_rules_set) - Replace inbound firewall rules

### [images](docs/sdks/images/README.md)

* [list_images](docs/sdks/images/README.md#list_images) - List available images

### [instances](docs/sdks/instances/README.md)

* [list_instances](docs/sdks/instances/README.md#list_instances) - List running instances
* [get_instance](docs/sdks/instances/README.md#get_instance) - Retrieve instance details
* [post_instance](docs/sdks/instances/README.md#post_instance) - Update instance details
* [list_instance_types](docs/sdks/instances/README.md#list_instance_types) - List available instance types
* [launch_instance](docs/sdks/instances/README.md#launch_instance) - Launch instances
* [restart_instance](docs/sdks/instances/README.md#restart_instance) - Restart instances
* [terminate_instance](docs/sdks/instances/README.md#terminate_instance) - Terminate instances


### [ssh_keys](docs/sdks/sshkeys/README.md)

* [list_ssh_keys](docs/sdks/sshkeys/README.md#list_ssh_keys) - List your SSH keys
* [add_ssh_key](docs/sdks/sshkeys/README.md#add_ssh_key) - Add an SSH key
* [delete_ssh_key](docs/sdks/sshkeys/README.md#delete_ssh_key) - Delete an SSH key

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK
from lambda_cloud_sdk.utils import BackoffStrategy, RetryConfig


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ),
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK
from lambda_cloud_sdk.utils import BackoffStrategy, RetryConfig


with LambdaCloudSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_instances_async` method may raise the following exceptions:

| Error Type                                        | Status Code | Content Type     |
| ------------------------------------------------- | ----------- | ---------------- |
| models.ListInstancesInstancesResponseBody         | 401         | application/json |
| models.ListInstancesInstancesResponseResponseBody | 403         | application/json |
| models.APIError                                   | 4XX, 5XX    | \*/\*            |

### Example

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK, models


with LambdaCloudSDK() as lcs_client:
    res = None
    try:

        res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
            basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
                username="",
                password="",
            ),
        ))

        # Handle response
        print(res)

    except models.ListInstancesInstancesResponseBody as e:
        # handle e.data: models.ListInstancesInstancesResponseBodyData
        raise(e)
    except models.ListInstancesInstancesResponseResponseBody as e:
        # handle e.data: models.ListInstancesInstancesResponseResponseBodyData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                          | Description                              |
| --- | ------------------------------- | ---------------------------------------- |
| 0   | `https://cloud.lambda.ai/`      | Production server                        |
| 1   | `https://cloud.lambdalabs.com/` | Secondary production server (deprecated) |

#### Example

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK(
    server_idx=1,
) as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK(
    server_url="https://cloud.lambda.ai/",
) as lcs_client:

    res = lcs_client.instances.list_instances(security=lambda_cloud_sdk.ListInstancesSecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ))

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from lambda_cloud_sdk import LambdaCloudSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = LambdaCloudSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from lambda_cloud_sdk import LambdaCloudSDK
from lambda_cloud_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = LambdaCloudSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `LambdaCloudSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from lambda_cloud_sdk import LambdaCloudSDK
def main():

    with LambdaCloudSDK() as lcs_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with LambdaCloudSDK() as lcs_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from lambda_cloud_sdk import LambdaCloudSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = LambdaCloudSDK(debug_logger=logging.getLogger("lambda_cloud_sdk"))
```

You can also enable a default debug logger by setting an environment variable `LAMBDACLOUDSDK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=lambda-cloud-sdk&utm_campaign=python)
