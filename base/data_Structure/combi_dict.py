# -*- coding:utf-8 -*-

a = {'x':1, 'z':2}
b = {'y':3, 'z':4}

from collections import ChainMap

c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

