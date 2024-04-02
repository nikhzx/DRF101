import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    '''
    App for GET method
    '''
    data = {}
    headers = {'content-Type':'application/json'} #its imp to give header with each api request using api_view
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, headers=headers, data = json_data)
    res = r.json()
    print(res)

# get_data(2)


def post_data():
    '''
    App for POST Method
    '''
    data = {
        'name':'Kittu',
        'roll': 7,
        'city': "Guisharnath"
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    res = r.json()
    print(res)

# post_data()
    
def update_data():
    '''
    App for PUT Method
    '''
    data = {
        'id':1,
        'name':"Nikhil", 
        # 'city':"Prayagraj",
        # 'roll':201
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    res = r.json() 
    print(res)

# update_data()
    
def delete_data(id):
    '''
    App for DELETE method
    '''
    data = {}
    # data = {'id':[11,13,14]}
    headers = {'content-Type':'application/json'}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    res = r.json()
    print(res)

delete_data(4)