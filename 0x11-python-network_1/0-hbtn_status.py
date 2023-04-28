#!/usr/bin/python3
# Write a Python script that fetches
import urllib.request


def display_info(response):
    body = response.read()
    print("- type: {}".format(type(body)))
    print("- content: {}".format(body))
    print("- utf8 content: {}".format(body.decode('utf-8')))


def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        display_info(response)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url(url)
