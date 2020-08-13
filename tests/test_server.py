import pytest
from server import __version__, app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_version():
    assert __version__ == '0.1.0'

def test_home_page(client):
    res = client.get('/')
    assert "200 OK"         in res.status
    assert b"_home page_"   in res.data

def test_hello_page(client):
    res = client.get('/hello')
    assert "200 OK"         in res.status
    assert b"hello world!"  in res.data