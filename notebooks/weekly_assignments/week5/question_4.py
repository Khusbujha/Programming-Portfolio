"""This program takes a URL as a command-line argument and reports whether or not there is a working website at that address."""

import sys
import urllib.request


def main():
    if len(sys.argv) < 2:
        print("Error: URL not provided!!!")
        sys.exit()
    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        print(f"Website at {url} is working (HTTP response code:{response.getcode()}).")
    except urllib.error.HTTPError as e:
        print(f"Website at {url} returned error code {e.code}.")
    except urllib.error.URLError as e:
        print(f"Website at {url} is not reachable.")


if __name__ == "__main__":
    main()
