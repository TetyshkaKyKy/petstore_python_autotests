from http import HTTPStatus
from src.my_requests import MyRequests
import jsonschema


def test_create_pet_with_required_parameters():
    response = MyRequests.post(
        '/pet',
        data={
            "name": "DOG",
            "photoUrls": [
                "https://bigpicture.ru/wp-content/uploads/2015/11/nophotoshop29-800x532.jpg"
            ]
        },
        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'DOG'
    assert response.json()['photoUrls'] == [
        'https://bigpicture.ru/wp-content/uploads/2015/11/nophotoshop29-800x532.jpg']


def test_create_pet_with_all_parameters():
    # create pet
    request_body = {
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
    response = MyRequests.post(
        '/pet',
        data=request_body,
        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )

    assert response.status_code == HTTPStatus.OK
    new_pet_id = response.json()['id']

    # check new pet
    response1 = MyRequests.get(
        f'/pet/{new_pet_id}'
    )

    expected_result = {
        "id": new_pet_id,
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
    jsonschema.validate(actual_result, schema)
    assert response1.status_code == HTTPStatus.OK
    assert expected_result == actual_result


'''
    Тест на создание питомца без обязательного параметра name или без обоих обязательных параметров будет идентичен. 
    Нет сообщения об ошибке, сущность создается
'''


def test_create_pet_wo_required_parameter_photoUrls():
    response = MyRequests.post(
        '/pet',
        data={
            "name": "DOG"
        },
        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )
    assert response.status_code == HTTPStatus.OK
