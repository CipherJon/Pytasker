from app import app, db
import pytest

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Task List" in response.data