from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

endpoint = '/courses/'
id_course = client.get(endpoint).json()[0]['id']
endpoint_one = f'{endpoint}{id_course}'

def test_courses_get_all():
    response = client.get(endpoint)
    assert response.status_code == 200
    assert type(response.json()) is list

def test_courses_get_one():
    response = client.get(endpoint_one)
    assert response.status_code == 200
    assert type(response.json()) is dict

def test_courses_post_one():
    response = client.post(endpoint, json={
        'title': 'Course 2',
        'description': '...',
        'hours': 15,
        'price': 199.19
    })
    fields = list(response.json().keys())

    assert response.status_code == 200
    assert sorted(fields) == sorted(['id', 'title', 'description', 'hours', 'price'])
    assert type(response.json()) is dict

def test_courses_delete_one():
    response = client.delete(endpoint_one)
    assert response.status_code == 200
    assert type(response.json()) is dict

    response = client.get(endpoint_one)
    assert response.status_code == 404

def test_courses_put_one():
    course_data = {
          'title': 'Course 3',
          'description': '...',
          'hours': 150,
          'price': 899
    }
    response = client.put(endpoint_one, json=course_data)
    assert response.status_code == 200
    assert type(response.json()) is dict

    assert response.json()['course'] == course_data
