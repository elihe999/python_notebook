# -*- coding: utf-8 -*-
"""

"""
import re

s1='PYTHON is amazing'
t1='python'
s2='python is amazing'
result = t1 in s1
print(result)
result = t1 in s2
print(result)

m = re.search('PYTHON', 'python is amazing', re.IGNORECASE)
print(m==None)
