from http.client import UNSUPPORTED_MEDIA_TYPE
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    '''
    App for GET method
    '''
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    res = r.json()
    print(res)

# get_data(2)


def post_data():
    '''
    App for POST Method
    '''
    data = {
        'name': "Arjun",
        'roll': "12",
        'city': "Hastinapur"
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    res = r.json()
    print(res)

# post_data()
    
def update_data():
    '''
    App for PUT Method
    '''
    data = {
        'id':9,
        # 'name':"Bheem", 
        # 'city':"Kurukshetra",
        'roll':13
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    res = r.json() 
    print(res)

update_data()