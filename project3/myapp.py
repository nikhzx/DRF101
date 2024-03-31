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

get_data()


def post_data():
    '''
    App for POST Method
    '''
    data = {
        'name': "Noikhil",
        'roll': 21,
        'city': "Prayag"
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    res = r.json()
    print(res)

post_data()
    
def update_data():
    '''
    App for PUT Method
    '''
    data = {
        'id':15,
        'name':"Jiya", 
        'city':"Prayagraj",
        'roll':201
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    res = r.json() 
    print(res)

# update_data()
    
def delete_data():
    '''
    App for DELETE method
    '''
    data = {'id':11}
    # data = {'id':[11,13,14]}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    res = r.json()
    print(res)

# delete_data()