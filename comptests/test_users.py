import requests

def test_users():
    r = requests.get("http://localhost:5000/users")

    assert r.status_code == 200
    