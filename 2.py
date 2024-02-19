import json
import sys
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("server", metavar="server", type=str)
parser.add_argument('port', metavar='port', type=str)
parser.add_argument('color', metavar='color', type=str, nargs='*')
parser.add_argument('--key', metavar='key', type=int, default=3)

args = parser.parse_args()
g = requests.get(f'http://{args.server}:{args.port}/')
data = g.json()
for i in data:
    for j in i:


