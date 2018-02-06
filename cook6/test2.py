'''

6.2 Reading and Writing JSON Data
'''

import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print('json_str:', json_str)
data = json.loads(json_str)

with open('data.json', 'w') as f:
    json.dump(data, f)


with open('data.json', 'r') as f:
    data = json.load(f)


# =========================================================

result1 = json.dumps(False)
print('result1:', result1)

d = {'a' : True,
     'b' : 'Hello',
     'c' : None}

result2 = json.dumps(d)
print('result2:', result2)

# =========================================================

from urllib.request import urlopen
import json
u = urlopen('https://api.androidhive.info/volley/person_object.json')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
pprint(resp)

# =========================================================
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print('data:', data)

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
name = data.name
shares = data.shares
price = data.price
print('data type:', type(data))
print(name, shares, price, sep=' ')

# =========================================================
data = json.loads(s, object_pairs_hook=OrderedDict)
print(json.dumps(data))
print(json.dumps(data, indent=4))
print(json.dumps(data, indent=4, sort_keys=True))

# =========================================================

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
p = Point(2, 3)
# json.dumps(p)

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

classes = {
    'Point': Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

s = json.dumps(p, default=serialize_instance)
print('s:', s)
a = json.loads(s, object_hook=unserialize_object)
print('a:', a)

print('a.x:', a.x)
print('a.y:', a.y)

