import requests
import json

response = requests.get('https://api.github.com/users/IIIu63uK')
data = response.json()

print(json.dumps(data, indent=4))