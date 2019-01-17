# -*- coding: utf-8 *-

"""
dist from json
"""

import json

with open('./test.json', 'r') as load_f:
    LOAD_DIST = json.load(load_f)
    
for NAME,VALUE in LOAD_DIST.items():
    print(NAME)
    print(VALUE)


