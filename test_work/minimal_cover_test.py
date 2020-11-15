# author:Boyle time:2020/11/15
import requests
import json
from pprint import pprint


host = "http://localhost:8000"


path = "/minimalCover/inputList"
req_url = host + path
data = json.dumps({
    "F": [{
        "V": ["A"],
        "W": ["B"]
    },{
        "V": ["A"],
        "W": ["C"]
    },{
        "V": ["B"],
        "W": ["A"]
    },{
        "V": ["B"],
        "W": ["C"]
    },{
        "V": ["C"],
        "W": ["A"]
    }]
})
ret = requests.post(req_url, data=data)
pprint(json.loads(ret.content))