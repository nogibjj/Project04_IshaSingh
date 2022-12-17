# %%

import requests
import json

def make_request():
    response = requests.delete('https://reqres.in/api/users/2')

    if (response.status_code != 204
            and 'content-type' in response.headers
            and 'application/json' in response.headers['content-type']):
        parsed = response.json()
    else:
        parsed = None
        


make_request()
url = 'http://localhost:8000/api'
r = requests.post(url,json={'exp':1.8,})
print(r.json())

# %%



