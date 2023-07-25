# ######Задача №1

import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)

for item in resp.json():
    if item['name'] == 'Hulk':
        Hulk_intelligence = item['powerstats']['intelligence']

    if item['name'] == 'Captain America':
        Captain_intelligence = item['powerstats']['intelligence']

    if item['name'] == 'Thanos':
        Thanos_intelligence = item['powerstats']['intelligence']

max_intelligence = max(Hulk_intelligence, Captain_intelligence, Thanos_intelligence)

if Hulk_intelligence == max_intelligence:
    pprint(f'Самый умный Hulk c интеллектом {Hulk_intelligence} ед.')
if Captain_intelligence == max_intelligence:
    pprint(f'Самый умный Captain America c интеллектом {Captain_intelligence} ед.')
if Thanos_intelligence == max_intelligence:
    pprint(f'Самый умный Thanos c интеллектом {Thanos_intelligence} ед.')

________________________________________________________________________________________________
#Задача №2
import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_link(self, file_path: str):
        '''Получаем ссылку на место на Яндекс.Диске'''

        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, file_path):
        '''Метод загружает файл на Яндекс.Диск'''

        href = self.upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open('test.txt', 'rb'))
        response.raise_for_status()
        # pprint(response)
        if response.status_code == 201:
            print('Файл загружен успешно!')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Нетология/test_20230720'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)