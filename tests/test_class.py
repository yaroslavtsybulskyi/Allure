import allure

from conftest import ApiClient


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("get request")
def test_get_(my_url):
    response = ApiClient.get(my_url)

    assert response.status_code == 200


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("post request")
def test_post(my_url):
    response = ApiClient.post(my_url)

    assert response.status_code == 200


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("put request")
def test_put(my_url):
    response = ApiClient.put(my_url)

    assert response.status_code == 200


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("patch request")
def test_patch(my_url):
    response = ApiClient.patch(my_url)

    assert response.status_code == 200


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("delete request")
def test_delete(my_url):
    response = ApiClient.delete(my_url)

    assert response.status_code == 200


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("head request")
def test_head(my_url):
    response = ApiClient.head(my_url)

    assert response.status_code == 404


@allure.epic("Api client")
@allure.description("simple req")
@allure.feature("options request")
def test_options(my_url):
    response = ApiClient.options(my_url)

    assert response.status_code == 404
