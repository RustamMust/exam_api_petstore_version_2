import allure
import pytest
import requests
from pydantic import ValidationError
from payloads.payloads import payload_create_object_200
from payloads.payloads import payload_update_object_200
from payloads.payloads import payload_update_object_405
from payloads.payloads import payload_empty
from payloads.payloads import payload_none
from payloads.payloads import payload_not_exist
from payloads.payloads import object_id_not_exist
from conftest import object_id
from models.response_object_model import Item
from conftest import BASE_URL



@allure.feature('Создание объекта')
@pytest.mark.parametrize("payload, expected_status_code", [
    (payload_create_object_200, 200),
    (payload_empty, 405),
    (payload_none, 415)
])
def test_create_object_all(payload, expected_status_code):
    with allure.step("Отправка POST-запроса"):
        response = requests.post(BASE_URL, json=payload)
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code
    try:
        Item.model_validate(response.json())
        print('Валидация прошла')
    except ValidationError:
        print('Валидация не прошла')


@allure.feature('Изменение объекта')
@pytest.mark.parametrize("payload, object_id, expected_status_code", [
    (payload_update_object_200, object_id, 200),
    (payload_update_object_405, object_id, 405),
    (payload_not_exist, object_id, 404),
    (payload_update_object_200, object_id_not_exist, 400)
])
def test_update_object_all(payload, object_id, expected_status_code):
    with allure.step("Отправка PUT-запроса"):
        response = requests.put(f'{BASE_URL}{object_id}', json=payload)
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code


@allure.feature('Получение объекта')
@pytest.mark.parametrize("status_endpoint, expected_status_code", [
    ('findByStatus?status=sold', 200),
    ('findByStatus?status=lost', 400)
])
def test_get_object_all(status_endpoint, expected_status_code):
    with allure.step("Отправка GET-запроса"):
        response = requests.get(f'{BASE_URL}{status_endpoint}')
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code
    try:
        Item.model_validate(response.json())
        print('Валидация прошла')
    except ValidationError:
        print('Валидация не прошла')


@allure.feature('Удаление объекта')
@pytest.mark.parametrize("obj_id, expected_status_code", [
    (object_id, 200),
    (object_id, 404),
    (object_id_not_exist, 400)
])
def test_delete_object_all(obj_id, expected_status_code):
    with allure.step("Отправка DELETE-запроса"):
        response = requests.delete(f'{BASE_URL}{obj_id}')
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code


