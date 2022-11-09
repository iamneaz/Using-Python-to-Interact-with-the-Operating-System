# import requests
# import socket


# def check_localhost():
#     localhost = socket.gethostbyname('localhost')
#     return localhost


# def check_connectivity():
#     request = requests.get("https://www.google.com")
#     websiteResponse = request.status_code
#     return websiteResponse

import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_connectivity():
    request = requests.get("http://www.google.com")
    return request.status_code == 200


print(check_localhost())
print(check_connectivity())
