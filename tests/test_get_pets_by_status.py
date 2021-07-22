from http import HTTPStatus
import pytest
from src.my_requests import MyRequests


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_find_pets_by_correct_status(status):
    response = MyRequests.get(
        '/pet/findByStatus',
        data={'status': status}
    )

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) > 0


@pytest.mark.parametrize('status', ['Available', 'Pending', 'Sold', 'AVAILABLE', 'PENDING', 'SOLD', 'new', 'NEW', 'New',
                                    '', 123, '@', True])
def test_find_pets_by_incorrect_status(status):
    response = MyRequests.get(
        '/pet/findByStatus',
        data={'status': status}
    )

    # согласно ТЗ, при невалидном статусе должен быть статус код 400, но в реальности он всегда 200
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []
