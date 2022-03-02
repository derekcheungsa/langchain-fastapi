import asyncio
from fastapi.testclient import TestClient
from app.main import app, root

client = TestClient(app)


def test_root():
    '''Test root function logic
    >>> asyncio.run(root())
    {'api': 'FastAPI Template'}
    '''
    result = asyncio.run(root())
    assert result == {'api': 'FastAPI Template'}

def test_root_endpoint():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'api': 'FastAPI Template'}

def test_courses_get_all():
    response = client.get('/courses')
    assert response.status_code == 200
    assert type(response.json()) is list

def test_courses_get_one():
    response = client.get('/courses/61d21fdc00988e6ca9284474')
    assert response.status_code == 200
    assert type(response.json()) is dict