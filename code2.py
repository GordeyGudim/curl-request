import requests
def test_access():
    headers = {
        'Accept': 'application/json',
        'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
        }

    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/files', headers=headers)
    return response