# SSHKey

Information about a stored SSH key, which can be used to access instances over
SSH.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The unique identifier (ID) of the SSH key.                                              | ddf9a910ceb744a0bb95242cbba6cb50                                                        |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | The name of the SSH key.                                                                | my-public-key                                                                           |
| `public_key`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | The public key for the SSH key.                                                         | ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICN+lJwsONkwrdsSnQsu1ydUkIuIg5oOC+Eslvmtt60T noname |