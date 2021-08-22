import datetime
from fastapi.testclient import TestClient


def test_display_time(test_client: TestClient, mocker):
    now = datetime.datetime.now()
    mocker.patch("app_python.display_time.MoscowTime.get_current_time", return_value=now)

    response = test_client.get("/")
    assert response.status_code == 200, response.text

    print(now)
    print(response.text)
    assert response.text == f"Current time in Moscow: {now.strftime('%Y-%m-%d %H:%M:%S')}"
