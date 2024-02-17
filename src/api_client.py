import json
import requests


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self):
        path = "get"
        url = self.base_address + path

        payload = {}
        headers = {
            'accept': 'application/json'
        }

        response = requests.request('GET', url, headers=headers, data=payload)
        return response

    def post(self):
        path = "post"
        url = self.base_address + path
        payload = json.dumps({
            "name": "Yaroslav",
            "email": "some@email.com"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def put(self):
        path = "put"
        url = self.base_address + path

        payload = json.dumps({
            "name": "Yaroslav",
            "lastname": "Last Name",
            "email": "email"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    def patch(self):
        path = "patch"
        url = self.base_address + path

        payload = json.dumps({
            "name": "Yaroslav",
            "lastname": "Last Name",
            "email": "test@email.com"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)

        return response

    def delete(self):
        path = "delete"
        url = self.base_address + path

        payload = json.dumps({
            "name": "Yaroslav"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        return response

    def head(self):
        path = "head"
        url = self.base_address + path

        payload = ""
        headers = {
            'accept': 'application/json'
        }

        response = requests.request("HEAD", url, headers=headers, data=payload)

        return response

    def options(self):
        path = "options"
        url = self.base_address + path

        payload = json.dumps({
            "name": "Yaroslav"
        })
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("OPTIONS", url, headers=headers, data=payload)

        return response
