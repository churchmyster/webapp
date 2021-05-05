import requests
import json

BASE = "http://0.0.0.0:3000/"

items = [{"id":25, "name": "Albert"},{"id":30, "name": "Mary"}]

response = requests.post(BASE + "items", json=items)

input()

response2 = requests.get(BASE + "items")

print(response2)

input()

response3 = requests.delete(BASE + "items")