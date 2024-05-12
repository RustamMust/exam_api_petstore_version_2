import pytest
import requests

BASE_URL = 'https://petstore.swagger.io/v2/pet/'


def object_id(payload_create_object_200):
    response = requests.post(BASE_URL, json=payload_create_object_200)
    return response['id']

