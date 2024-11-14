# Core Python Util
Embrace simplicity and efficiency – say NO to external Python packages for smaller projects! 🔥

This repository contains various Python utility functions for common tasks such as encryption, decryption, OTP generation, HTTP requests, and list shuffling.

## Table of Contents

- [Functions](#functions)
  - [One-Time Password (OTP) Generation](#one-time-password-otp-generation)
  - [HTTP Requests](#http-requests)
  - [List Shuffling](#list-shuffling)
  - [Simple HTTP Server](#simple-http-server)
- [Usage Examples](#usage-examples)
- [License](#license)

## Functions

### One-Time Password (OTP) Generation

#### `number_otp(length: int = 4)`

Generates a numeric OTP (One-Time Password) of a specified length.

- **Parameters**:
  - `length` (int): The length of the OTP to generate. Default is 4.

- **Returns**:
  - `str`: The generated OTP.

#### `mixed_otp(length: int = 5)`

Generates a mixed alphanumeric OTP (One-Time Password) of a specified length.

- **Parameters**:
  - `length` (int): The length of the OTP to generate. Default is 5.

- **Returns**:
  - `str`: The generated OTP.

### HTTP Requests

#### `get_request(url: str)`

Makes a GET request to the specified URL and prints the response.

- **Parameters**:
  - `url` (str): The URL to which the GET request is made.

#### `post_request(url: str, data: dict)`

Makes a POST request to the specified URL with the given data and prints the response.

- **Parameters**:
  - `url` (str): The URL to which the POST request is made.
  - `data` (dict): The data to be sent in the POST request.

#### `put_request(url: str, data: dict)`

Makes a PUT request to the specified URL with the given data and prints the response.

- **Parameters**:
  - `url` (str): The URL to which the POST request is made.
  - `data` (dict): The data to be sent in the POST request.

#### `patch_request(url: str, data: dict)`

Makes a PATCH request to the specified URL with the given data and prints the response.

- **Parameters**:
  - `url` (str): The URL to which the POST request is made.
  - `data` (dict): The data to be sent in the POST request.

#### `delete_request(url: str, data: dict)`

Makes a DELETE request to the specified URL with the given data and prints the response.

- **Parameters**:
  - `url` (str): The URL to which the POST request is made.

### List Shuffling

#### `shuffle_list(arr: list)`

Shuffles a list using a pseudo-random number generator based on the current time.

- **Parameters**:
  - `arr` (list): The list to be shuffled.

- **Returns**:
  - `list`: A new list with the elements shuffled.

### Simple HTTP Server

#### `SimpleHTTPRequestHandler`

A basic HTTP server example that serves a simple "Hello, World!" HTML page.

- **Usage**:
  - Run the server using `python -m web_server.server`.
  - Open a web browser and visit `http://localhost:8000` to see the served page.

## Usage Examples

### Example 1: Generating OTPs

```python
from otp_generator.number import number_otp

number_otp = number_otp(length=5)
print(f"Numeric OTP: {number_otp}")


from otp_generator.mixed import mixed_otp

mixed_otp = mixed_otp(length=5)
print(f"Mixed OTP: {mixed_otp}")
```

### Example 2: Making HTTP Requests

```python
from request.get import get_request

url = 'https://servebin.dev/json'
get_request(url)


from request.post import post_request

post_url = 'https://servebin.dev/post'
post_data = {'key': 'value'}
post_request(post_url, post_data)


from request.delete import delete_request

delete_url = 'https://servebin.dev/delete'
delete_request(delete_url)


from request.put import put_request

put_url = 'https://servebin.dev/put'
put_data = {'key': 'new_value'}
put_request(put_url, put_data)


from request.patch import patch_request

patch_url = 'https://servebin.dev/patch'
patch_data = {'key': 'modified_value'}
patch_request(patch_url, patch_data)
```

### Example 3: Shuffling a List

```python
from core_random.shuffle import shuffle_list

my_list = [1, 2, 3, 4, 5]
shuffled = shuffle_list(my_list)
print(f"Original List: {my_list}")
print(f"Shuffled List: {shuffled}")
```

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.
