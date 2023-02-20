import json

json_str = json.dumps([1,2,3])
print(json_str)

py_obj = json.loads(json_str)
print(py_obj)