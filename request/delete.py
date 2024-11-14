#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import json
import urllib.error
import urllib.request


def delete_request(url: str) -> None:
    """
    Makes a DELETE request to the specified URL and prints the response.

    Args:
        url (str): The URL to which the request is made.

    Raises:
        urllib.error.URLError: If the request fails.
    """
    try:
        # Create a Request object with DELETE method
        request = urllib.request.Request(url, method="DELETE")

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
    url = "https://servebin.dev/delete"
    delete_request(url)
