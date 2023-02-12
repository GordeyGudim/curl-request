import requests
from http import HTTPStatus
from urllib.parse import quote, urlencode
from urllib import request
import json
import webbrowser
import os

class YaDisk():
    AUTH_URL = 'https://oauth.yandex.ru/authorize'
    TOKEN_URL = 'https://oauth.yandex.ru/token'

    CLIENT_ID = 'b69d36bdd5074a1ba7d017995e69f728'
    CLIENT_NOT_SO_SECRET = '6c472ab5cb1b424783447c6962906dcb'

    LIST_FOLDER_URL = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    # def _request(self):
    #     grant_type = authorization_code
    #     code = <код_подтверждения>
    #     client_id = <идентификатор_приложения>
    #     client_secret = <пароль_приложения>
    def __init__(self, camera_id=None):
            self._location = None
            self._authorization_key = None
            self._credentials = None
            #UploadService.__init__(self, camera_id)   
    def request(self, url, headers=None, params = None, files=None):
        response = requests.put(url, headers=headers, params=params, files=files)
        if response.status_code != 200:
            response = requests.get(url, headers=headers, params=params, files=files)
        return response
    def test_access(self):
            url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
            headers = {
                'Accept': 'application/json',
                'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
            }
                
            response = self.request(url, headers)

            try:
                response.raise_for_status()
                return response.status_code
            except requests.exceptions.HTTPError:
                return f'Failed: {response.status_code}'
    def get_authorize_url(self):
            query = {
            'response_type': 'code',
            'client_id': 'b69d36bdd5074a1ba7d017995e69f728',
            }
            return 'https://oauth.yandex.ru/authorize'+'?'+urlencode(query)
    def token(self, url='https://oauth.yandex.ru/token'):
        url = 'https://oauth.yandex.ru/authorize?response_type=code&client_id=b69d36bdd5074a1ba7d017995e69f728'
        # короче дописать чутка там надо попробовать с кодом рещить ага вот ссылка: https://yandex.ru/dev/direct/doc/examples-v5/python3-requests-token.html
        a = self.request(url)
        print (a.text)


    def creat_folder(self):
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
        }

        params = {
        'path': 'nowdata'
        }

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
    

    def upload_data(self, filename,mime_type=None, data=None, ctime=None, camera_name=None):
        self.creat_folder()
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
        'Accept': 'application/json',
        'Authorization': 'OAuth y0_AgAAAABmjXc-AAi5VAAAAADVUQoRoQpQsEdvSaWgsGhVPKQoLzOb_BQ',
        }
        
        params = {
            'path': f'nowdata/{filename}'
        }
        response = self.request(url, headers, params)
        return response.json()
    def load(self, filename):
        url = self.upload_data(filename)['href']
        with open('txt.txt', 'rb+') as f:
            files ={'file': f}
            self.request(url, files = files)
        #     resp = requests.put(self.upload_data(filename)['href'], files={'file': f})
test = YaDisk()
n = test.token()
print(n)


