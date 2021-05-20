import requests
from http import HTTPStatus
from src.services import base_url
from deepdiff import DeepDiff

def test_create_pet_with_required_parameters():
    response = requests.post(
        url=f'{base_url}/pet',
        json={
            "name": "DOG",
            "photoUrls": [
                "https://bigpicture.ru/wp-content/uploads/2015/11/nophotoshop29-800x532.jpg"
            ]
        },
        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'DOG'
    assert response.json()['photoUrls'] == ['https://bigpicture.ru/wp-content/uploads/2015/11/nophotoshop29-800x532.jpg']


def test_create_pet_with_all_parameters():
    request_body = {
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
    response = requests.post(
        url=f'{base_url}/pet',
        json=request_body,
        headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )
    actual_result = response.json()
    diff = DeepDiff(request_body, actual_result)
    assert response.status_code == HTTPStatus.OK
    assert not diff, diff.pretty()

#Тест на создание питомца без обязательного параметра name или без обоих обязательных параметров будет идентичен
#Нет сообщения об ошибке, сущность создается
def test_create_pet_without_required_parameter_photoUrls():
    response = requests.post(
    url=f'{base_url}/pet',
    json={
        "name": "DOG"
    },
    headers={'accept': 'application/json', 'Content-Type': 'application/json'}
    )
    assert response.status_code == HTTPStatus.OK






