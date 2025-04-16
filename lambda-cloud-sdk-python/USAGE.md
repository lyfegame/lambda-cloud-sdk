<!-- Start SDK Example Usage [usage] -->
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