import allure
import requests
import json



@allure.feature("api-testing")
@allure.title("Get Request")
def test_get(base_url):
    # curl -X GET "https://httpbin.org/get" -H "accept: application/json"
    url = base_url + "get"

    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200


@allure.title("Post Request")
def test_post(base_url):
    # curl -X POST "https://httpbin.org/post" -H "accept: application/json"

    url = base_url + "post"

    payload = json.dumps({
        "name": "Yaroslav",
        "email": "some@email.com"
    })
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200


@allure.feature("api-testing")
@allure.title("Put Request")
def test_put(base_url):
    # curl -X PUT "https://httpbin.org/put" -H "accept: application/json"

    url = base_url + "put"

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

    assert response.status_code == 200


@allure.title("Delete Request")
def test_delete(base_url):
    # curl -X DELETE "https://httpbin.org/delete" -H "accept: application/json"

    url = base_url + "delete"

    payload = json.dumps({
        "name": "Yaroslav"
    })
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    assert response.status_code == 200


@allure.title("Patch Request")
def test_patch(base_url):
    # curl -X PATCH "https://httpbin.org/patch" -H "accept: application/json"

    url = base_url + "patch"

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

    assert response.status_code == 200


@allure.title("Head Request")
@allure.description("Status code should be 404")
def test_head(base_url):
    url = base_url + "head"

    payload = ""
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("HEAD", url, headers=headers, data=payload)

    assert response.status_code == 404


@allure.title("Options Request")
@allure.description("Status code should be 404")
def test_options(base_url):
    url = base_url + "options"

    payload = json.dumps({
        "name": "Yaroslav"
    })
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("OPTIONS", url, headers=headers, data=payload)

    assert response.status_code == 404
