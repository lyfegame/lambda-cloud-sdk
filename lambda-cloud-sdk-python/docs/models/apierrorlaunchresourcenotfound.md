# APIErrorLaunchResourceNotFound


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `code`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | The unique identifier for the type of error.               |
| `message`                                                  | *str*                                                      | :heavy_check_mark:                                         | The resource the API was unable to find.                   |
| `suggestion`                                               | *str*                                                      | :heavy_check_mark:                                         | One or more suggestions of possible ways to fix the error. |