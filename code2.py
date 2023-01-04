import requests
from http import HTTPStatus
from urllib.parse import quote, urlencode
from urllib import request
import json

import os
class YaDisk():
    AUTH_URL = 'https://oauth.yandex.ru/authorize'
    #TOKEN_URL = 'https://oauth.yandex.ru/authorize?response_type=token'

    CLIENT_ID = 'b69d36bdd5074a1ba7d017995e69f728'
    CLIENT_NOT_SO_SECRET = '6c472ab5cb1b424783447c6962906dcb'

    LIST_FOLDER_URL = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'





    def __init__(self, camera_id):
            self._location = None
            self._authorization_key = None
            self._credentials = None

            UploadService.__init__(self, camera_id)
    def test_access():
            url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
            data = {
                'Accept': 'application/json',
                'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
            }
            response = requests.get(url, headers=data)
            try:
                response.raise_for_status()
                return response.status_code
            except requests.exceptions.HTTPError:
                return f'Failed: {response.status_code}'
def get_authorize_url():
        query = {
        'response_type': 'code',
        'client_id': 'b69d36bdd5074a1ba7d017995e69f728',
        }
        data = {
                'Accept': 'application/json',
                #'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
            }
        return 'https://oauth.yandex.ru/authorize'+'?'+urlencode(query)
        #print(req.text)
        
print(get_authorize_url())



def upload_data(self, filename, mime_type, data, ctime, camera_name):
    headers = {
    'Accept': 'application/json',
    'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
    }
    params = {
        'path': filename,
    }
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params=params, headers=headers)
    return response.json()
def load():
    with open('downloaded_file.jpg', 'rb+') as f:
        resp = requests.put(upload_data()['href'], files={'file': f})
