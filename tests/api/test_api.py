from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "AI Fake News Detection API"
    }


def test_get_users():

    response = client.get("/api/users")

    assert response.status_code == 200


def test_create_user():

    response = client.post("/api/users")

    assert response.status_code == 200

    assert response.json() == {
        "message": "User created"
    }


def test_get_articles():

    response = client.get("/api/articles")

    assert response.status_code == 200


def test_create_article():

    response = client.post("/api/articles")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Article created"
    }


def test_get_results():

    response = client.get("/api/results")

    assert response.status_code == 200


def test_create_result():

    response = client.post("/api/results")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Result created"
    }


def test_update_user():

    response = client.put("/api/users/1")

    assert response.status_code == 200


def test_delete_user():

    response = client.delete("/api/users/1")

    assert response.status_code == 200


def test_analyze_article():

    response = client.post("/api/articles/1/analyze")

    assert response.status_code == 200

    data = response.json()

    assert data["classification"] == "Fake"


def test_update_article():

    response = client.put("/api/articles/1")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Article updated"
    }


def test_delete_article():

    response = client.delete("/api/articles/1")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Article deleted"
    }


def test_update_result():

    response = client.put("/api/results/1")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Result updated"
    }


def test_delete_result():

    response = client.delete("/api/results/1")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Result deleted"
    }