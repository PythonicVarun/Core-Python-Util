#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import json
import urllib.error
import urllib.parse
import urllib.request


def post_request(url: str, data: dict) -> None:
    """
    Makes a POST request to the specified URL with the given data and prints the response.

    Args:
        url (str): The URL to which the request is made.
        data (dict): The data to be sent in the POST request.

    Raises:
        urllib.error.URLError: If the request fails.
    """
    try:
        # Encode the data
        encoded_data = urllib.parse.urlencode(data).encode()

        # Create a Request object
        request = urllib.request.Request(url, data=encoded_data, method="POST")
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
    url = "https://servebin.dev/post"
    data = {"key1": "value1", "key2": "value2"}
    post_request(url, data)
