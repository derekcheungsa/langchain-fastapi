from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

PATH = '/cards/'
id_card = client.get(PATH).json()[0]['id']
PATH_one = f'{PATH}{id_card}'

def test_get_cards_all():
    response = client.get(PATH)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_cards_one():
    response = client.get(PATH_one)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_cards_slice():
    response = client.get(f'{PATH}slice', params={'start': 0, 'end': 2})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cards_post_one():
    response = client.post(PATH, json={
        'title': 'Card 2',
        'description': '...',
        'hours': 15,
        'price': 199.19
    })
    fields = list(response.json().keys())

    assert response.status_code == 200
    assert sorted(fields) == sorted(['id', 'title', 'description', 'hours', 'price'])
    assert isinstance(response.json(), dict)

def test_cards_delete_one():
    response = client.delete(PATH_one)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    response = client.get(PATH_one)
    assert response.status_code == 404

def test_cards_put_one():
    card_data = {
          'title': 'Card 3',
          'description': '...',
          'hours': 150,
          'price': 899
    }
    response = client.put(PATH_one, json=card_data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

    assert response.json()['card'] == card_data
