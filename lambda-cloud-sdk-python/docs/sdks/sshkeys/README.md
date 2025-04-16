# SSHKeys
(*ssh_keys*)

## Overview

### Available Operations

* [list_ssh_keys](#list_ssh_keys) - List your SSH keys
* [add_ssh_key](#add_ssh_key) - Add an SSH key
* [delete_ssh_key](#delete_ssh_key) - Delete an SSH key

## list_ssh_keys

Retrieves a list of your SSH keys.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.ssh_keys.list_ssh_keys(security=lambda_cloud_sdk.ListSSHKeysSecurity(
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
| `security`                                                          | [models.ListSSHKeysSecurity](../../listsshkeyssecurity.md)          | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSSHKeysResponseBody](../../models/listsshkeysresponsebody.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.ListSSHKeysSSHKeysResponseBody         | 401                                           | application/json                              |
| models.ListSSHKeysSSHKeysResponseResponseBody | 403                                           | application/json                              |
| models.APIError                               | 4XX, 5XX                                      | \*/\*                                         |

## add_ssh_key


Add an SSH key to your Lambda Cloud account. You can upload an existing public
key, or you can generate a new key pair.

-  To use an existing key pair, set the `public_key` property in the request body
   to your public key.

-  To generate a new key pair, omit the `public_key` property from the request
   body.

<div style="border: 0.075rem solid #E48603; border-radius: .2rem; font-size: 13px;
  box-shadow: 0 0.2rem 0.5rem #0000000d,0 0 0.05rem #0000001a">
  <div style="background-color: #E486031a; padding: .4rem 2rem .4rem .6rem; font-weight: bold;">Important</div>
  <div style="background-color: transparent; padding: .4rem .6rem; line-height: 1.4;">Lambda doesn't
  store your private key after it's been generated. If you generate a new key pair, make sure to save
  the resulting private key locally.</div>
</div>

For example, to generate a new key pair and associate it with a Lambda
On-Demand Cloud instance:

1. Generate the key pair. The command provided below automatically extracts and
    saves the returned private key to a new file called `key.pem`. Replace
    `<NEW-KEY-NAME>` with the name you want to assign to the SSH key:

    ```
    curl https://cloud.lambda.ai/api/v1/ssh-keys \
    --fail \
    -u ${LAMBDA_API_KEY}: \
    -X POST \
    -d '{"name": "<NEW-KEY-NAME>"}' \
    | jq -r '.data.private_key' > key.pem
    ```

2. Next, set the private key's permissions to read-only:

    ```
    chmod 400 key.pem
    ```

3. Launch a new instance. Replace `<NEW-KEY-NAME>` with the name you assigned
   to your SSH key.

    ```
    curl -X POST "https://cloud.lambda.ai/api/v1/instance-operations/launch" \
    --fail \
    -u ${LAMBDA_API_KEY}: \
    -X POST \
    -d '{"region_name":"us-west-1","instance_type_name":"gpu_1x_a10","ssh_key_names":["<NEW-KEY-NAME>"],"file_system_names":[],"quantity":1,"name":"My Instance"}'
    ```

4. From your local terminal, establish an SSH connection to the instance.
   Replace `<INSTANCE-IP>` with the public IP of the instance:

    ```
    ssh -i key.pem <INSTANCE-IP>
    ```


### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.ssh_keys.add_ssh_key(security=lambda_cloud_sdk.AddSSHKeySecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), name="my-public-key", public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICN+lJwsONkwrdsSnQsu1ydUkIuIg5oOC+Eslvmtt60T noname")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.AddSSHKeySecurity](../../models/addsshkeysecurity.md)                           | :heavy_check_mark:                                                                      | N/A                                                                                     |                                                                                         |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | The name of the SSH key.                                                                | my-public-key                                                                           |
| `public_key`                                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The public key for the SSH key.                                                         | ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICN+lJwsONkwrdsSnQsu1ydUkIuIg5oOC+Eslvmtt60T noname |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.AddSSHKeyResponseBody](../../models/addsshkeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.AddSSHKeySSHKeysResponse400ResponseBody | 400                                            | application/json                               |
| models.AddSSHKeySSHKeysResponseBody            | 401                                            | application/json                               |
| models.AddSSHKeySSHKeysResponseResponseBody    | 403                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## delete_ssh_key

Deletes the specified SSH key.

### Example Usage

```python
import lambda_cloud_sdk
from lambda_cloud_sdk import LambdaCloudSDK


with LambdaCloudSDK() as lcs_client:

    res = lcs_client.ssh_keys.delete_ssh_key(security=lambda_cloud_sdk.DeleteSSHKeySecurity(
        basic_auth=lambda_cloud_sdk.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.DeleteSSHKeySecurity](../../models/deletesshkeysecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSSHKeyResponseBody](../../models/deletesshkeyresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.DeleteSSHKeySSHKeysResponse400ResponseBody | 400                                               | application/json                                  |
| models.DeleteSSHKeySSHKeysResponseBody            | 401                                               | application/json                                  |
| models.DeleteSSHKeySSHKeysResponseResponseBody    | 403                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |