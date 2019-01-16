#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Eli

keyword = []
keyword.append('World')
print(keyword)
keyword.append('new')
del keyword[1]
print(keyword)

secondKey = ['test', 'update', 'function']
print(len(secondKey))
print(keyword + secondKey)
print('test' in secondKey)
for word in secondKey:
    print(word)
