from http import HTTPStatus
import pytest
from src.my_requests import MyRequests


@pytest.mark.parametrize('id', ['-1', '0', '6954'])
def test_get_pet_by_incorrect_or_non_existent_id(id):
    response = MyRequests.get(
        '/pet/' + id
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'Pet not found'


def test_get_pet_by_string_id():
    response = MyRequests.get(
        '/pet/"one"'
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_pet_without_id():
    response = MyRequests.get(
        '/pet'
    )

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
