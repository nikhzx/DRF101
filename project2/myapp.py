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

# get_data(15)


def post_data():
    '''
    App for POST Method
    '''
    data = {
        'name': "Nikhil",
        'roll': "21",
        'city': "Prayagraj"
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
        'id':15,
        'name':"Nikhil", 
        'city':"Prayagraj",
        'roll':14
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    res = r.json() 
    print(res)

update_data()
    
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