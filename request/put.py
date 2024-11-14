#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import json
import urllib.error
import urllib.request


def put_request(url: str, data: dict) -> None:
    """
    Makes a PUT request to the specified URL with the given data and prints the response.

    Args:
        url (str): The URL to which the request is made.
        data (dict): The data to be sent in the PUT request.

    Raises:
        urllib.error.URLError: If the request fails.
    """
    try:
        # Serialize data if sending JSON
        data_bytes = json.dumps(data).encode()  # Serialize to JSON bytes

        # Create a Request object with PUT method
        request = urllib.request.Request(url, data=data_bytes, method="PUT")
        # Add header if sending JSON
        request.add_header("Content-Type", "application/json")

        # Make the request
        with urllib.request.urlopen(request) as response:
            html = response.read()
            headers = response.headers
            response = html.decode()
            if "application/json" in headers["content-type"]:
                try:
                    res_json = json.loads(response)
                    print(json.dumps(res_json, indent=4))
                except Exception as e:
                    print("Invalid JSON response:", e)
                    print(response)
            else:
                print(response)
    except urllib.error.URLError as e:
        print(f"Failed to make request: {e.reason}")


# Example usage:
if __name__ == "__main__":
    url = "https://servebin.dev/put"
    data = {"key1": "value1", "key2": "value2"}
    put_request(url, data)
