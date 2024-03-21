import json
import requests

URL = ""
data = {
    'name':'Sujay',
    'roll':107,
    'city':'South'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data= json_data)
data = r.json()
print(data)