import requests
import json

from requests import post

print(requests.get(f'http://127.0.0.1:5000/api/jobs').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/1').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/12321312').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/asdasdasdas').json())


"""print(post('http://127.0.0.1:5000/api/jobs', json={}).json())

print(post('http://127.0.0.1:5000/api/jobs',
           json={'job': 'Заголовок'}).json())"""

print(post('http://127.0.0.1:5000/api/jobs',
           json={'job': 'Заголовок',
                 'team_leader': 1,
                 'collaborators': 'Текст новости',
                 'work_size': 1,
                 'is_finished': False}).json())


print(requests.get('http://127.0.0.1:5000/api/v2/user').json())
print(post('http://127.0.0.1:5000/api/jobs',
           json={'surname': 'ishacovich',
                 'name': 'ishak',
                 'age': 122,
                 'position': 'asdsad',
                 'speciality': 'sdad',
                 'address':'sadasdas',
                 'email': 'q@2wqw',
                 'passswird': 1}).json())