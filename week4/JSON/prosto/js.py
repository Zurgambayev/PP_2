import json

data = {
     'user': 'zein',
     'text': 'hello',
     'attachments': ['1.png', '2.wav'],
     'type': 'direct',
     'demolition': None
}
    
jsn_str = json.dumps(data, sort_keys=True, indent=5)


with open('test_json.json', 'w') as f:
    json.dump(jsn_str, f,indent=5)

print(jsn_str)

