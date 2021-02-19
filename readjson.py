import json
with open("metadata.json",'r') as load_f:
    load_dict = json.load(load_f)

for key, dict in enumerate(load_dict):
    print(dict)


