# LambdaCloudSDK

## Overview

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



### Available Operations
