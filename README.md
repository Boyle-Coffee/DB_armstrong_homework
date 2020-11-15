# 数据库数据依赖的公理系统作业

服务地址：http://120.79.50.99:8000

## 求解闭包

### 接口1

**简要描述：**

- 以列表形式输入和返回$F$中的依赖

**请求路径：**

`http://127.0.0.1:5000/closure/inputList`

**请求方式：**

- POST

**输入参数（json）：**

```json
{
    "X": <array> "列表形式的属性集，如 ['A', 'B', 'c']",
    "F": <array> "函数依赖集列表，每个元素对象代表一个函数依赖"[{
        "V": <array> "函数依赖的决定因素，如 ['A', 'B']",
        "W": <array> "函数依赖于V的属性集，如 ['C']"
    }]
}
```

**输出参数（json）：**

```json
{
    "isSuccess": <boolean> "成功与否",
    "code": <int> "返回码",
    "message": <string> "返回信息说明",
    "data": <array> "属性集X关于函数依赖集F的闭包"
}
```

**测试样例：**

```python
import requests
import json
from pprint import pprint


host = "http://localhost:5000"


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
```

运行结果

```bash
{'code': 200,
 'data': ['A', 'C', 'E', 'B', 'D'],
 'isSuccess': True,
 'message': None}
```



## 求解最小依赖集

### 接口2

**简要描述：**

- 

**请求路径：**

`http://127.0.0.1:5000/minimalCover/inputList`

**请求方式：**

- POST

**输入参数（json）：**

```json
{
    "F": <array> "函数依赖集列表，每个元素对象代表一个函数依赖"[{
        "V": <array> "函数依赖的决定因素，如 ['A', 'B']",
        "W": <array> "函数依赖于V的属性集，如 ['C']"
    }]
}
```

**输出参数（json）：**

```json
{
    "isSuccess": <boolean> "成功与否",
    "code": <int> "返回码",
    "message": <string> "返回信息说明",
    "data": <array> {
        "F_m{}"%i: <array> "某个最小依赖集，i为第几个最小依赖集" [{
        	"V": <array> "函数依赖的决定因素，如 ['A', 'B']",
        	"W": <array> "函数依赖于V的属性集，如 ['C']"
        }]
    } 
}
```

**测试样例：**

```python
import requests
import json
from pprint import pprint


host = "http://localhost:5000"


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
```

运行结果

```bash
{'code': 200,
 'data': {'F_m1': [{'V': ['C'], 'W': ['A']},
                   {'V': ['A'], 'W': ['C']},
                   {'V': ['B'], 'W': ['A']},
                   {'V': ['A'], 'W': ['B']}],
          'F_m2': [{'V': ['B'], 'W': ['C']},
                   {'V': ['A'], 'W': ['B']},
                   {'V': ['C'], 'W': ['A']}]},
 'isSuccess': True,
 'message': None}
```

