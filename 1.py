import requests
import json
import csv

r = requests.get('http://127.0.0.1:8080/')

answer = {}

with open('asda.csv', 'r') as file:
    data = list(csv.DictReader(file, delimiter='-'))
c = 0

for i in data:
    c += 1
    answer[f'{c}'] = {}
    for j in i:
        if j != 'id' and j != 'height':
            answer[f'{c}'][j] = i[j]
with open('abc.json', 'w') as file:
    json.dump(answer, file)