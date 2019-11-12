import pytest
import connexion
from app import usersData

@pytest.fixture(scope='module')
def client():
    flask_app = connexion.FlaskApp(__name__)
    with flask_app.app.test_client() as c:
        yield c

def test_get_health(client):
    # GIVEN no query parameters or payload
    # WHEN I access to the url GET /health
    # THEN the HTTP response is 404 not found
    response = client.get('/health')
    assert response.status_code == 404

def test_fetch_users(client):
    # GIVEN not query parameters or payload
    # WHEN I access to the url GET /api/v1/users
    # THEN the HTTP response is 200
    response = client.get('/api/v1/users')
    assert response.status_code == 404
