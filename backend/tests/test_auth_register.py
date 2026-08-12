import os

os.environ['USE_MONGO_MOCK'] = '1'

from app import app as flask_app
from models.db import users


def test_register_accepts_passenger_role_without_vehicle():
    users.delete_many({})
    client = flask_app.test_client()

    response = client.post('/api/auth/register', json={
        'name': 'Passenger User',
        'email': 'passenger@rvce.edu.in',
        'password': 'Pass123!',
        'college': 'RVCE',
        'year': '2nd',
        'branch': 'CSE',
        'phone': '9999999999',
        'role': 'passenger',
    })

    assert response.status_code == 201
    saved_user = users.find_one({'email': 'passenger@rvce.edu.in'})
    assert saved_user is not None
    assert saved_user['role'] == 'passenger'
