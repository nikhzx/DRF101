import requests
import json

URL = "http://127.0.0.1:8000/studetail/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    res = r.json()
    print(res)

get_data(2)

    