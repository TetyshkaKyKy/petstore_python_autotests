import requests
import jsonschema
from http import HTTPStatus
from src.services import base_url
import pytest



def test_get_pet_by_id_structure():
    response = requests.get(
        url=f'{base_url}/pet/14'
    )
    expected_result = {
            "id": 14,
            "category": {
                "id": 1,
                "name": "DOG"
            },
            "name": "DOG",
            "photoUrls": [
                "https://clck.ru/UhnQT"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "new_tag"
                }
            ],
            "status": "available"
        }
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'category': {'type': 'object',
                         'properties': {
                             'id': {'type': 'integer'},
                             'name': {'type': 'string'}
                         }
                         },
            'name': {'type': 'string'},
            'photoUrls': {'type': 'array',
                          'items': {'type': 'string'}
                          },
            'tags': {'type': 'array',
                     'items': {'type': 'object'},
                     'properties': {
                            'id': {'type': 'integer'},
                            'name': {'type': 'string'}
                        }
                     },
            'status': {'type': 'string'}
        }
    }
    actual_result = response.json()
    jsonschema.validate(response.json(), schema)
    response.status_code == HTTPStatus.OK
    expected_result == actual_result


@pytest.mark.parametrize('id',['-1','0','6954'])
def test_get_pet_by_incorrect_or_non_existent_id(id):
    response = requests.get(
        url=f'{base_url}/pet/' + id
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'

def test_get_pet_by_string_id():
    response = requests.get(
        url=f'{base_url}/pet/"one"'
        )
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_get_pet_without_id():
    response = requests.get(
        url=f'{base_url}/pet'
        )
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


