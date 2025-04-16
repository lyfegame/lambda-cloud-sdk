# InstanceType


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the instance type.                             | gpu_8x_h100_sxm5gdr                                        |
| `description`                                              | *str*                                                      | :heavy_check_mark:                                         | A description of the instance type.                        | 8x H100 (80 GB SXM5)                                       |
| `gpu_description`                                          | *str*                                                      | :heavy_check_mark:                                         | The type of GPU used by this instance type.                | H100 (80 GB SXM5)                                          |
| `price_cents_per_hour`                                     | *int*                                                      | :heavy_check_mark:                                         | The price of the instance type in US cents per hour.       | 3592                                                       |
| `specs`                                                    | [models.InstanceTypeSpecs](../models/instancetypespecs.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |