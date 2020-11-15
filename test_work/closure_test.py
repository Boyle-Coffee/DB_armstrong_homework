# author:Boyle time:2020/11/15
import requests
import json
from pprint import pprint


host = "http://localhost:8000"


path = "/closure/inputList"
req_url = host + path
data = json.dumps({
    "X": ["A", "B"],  # X = {A, B}
    "F": [{  # F = {AB→C, B→D, C→E, EC→B, AC→B}
        "V": ["A", "B"],
        "W": ["C"]
    },{
        "V": ["B"],
        "W": ["D"]
    },{
        "V": ["C"],
        "W": ["E"]
    },{
        "V": ["E", "C"],
        "W": ["B"]
    },{
        "V": ["A", "C"],
        "W": ["B"]
    }]
})
ret = requests.post(req_url, data=data)
pprint(json.loads(ret.content))