# -*- coding:utf-8 -*-

from collections import OrderedDict

d = OrderedDict()
d['fpp'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

import json
print(json.dumps(d))
