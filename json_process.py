# -*- coding: UTF-8 -*-
import json

# read json file
with open("metadata.json",'r') as load_f:
    load_dict = json.load(load_f)

# delete dict element    
load_dict.pop("del element")

# go through dict
for key, dict in enumerate(load_dict):
    print(dict)

# write json file    
with open("metadata.json",'w') as dump_f:
    json.dump(load_dict, dump_f)


