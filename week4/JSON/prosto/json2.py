import json


class myEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,set):
           return list(o) 

        return o

# data = {
#     'user ': 'zein',
#     'text':'hello',
#     'attachmants':['1 png','2.wav'],
#     'type':'direct',
#     'demolition': None

# }

jsn_str = json.dumps({1,2,3},cls = myEncoder)   #из py_object в json_str
print(jsn_str)