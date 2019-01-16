#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

var1 = 'Hello World!' 
print(var1[:6] + 'Runoob!')

if 'World!' in var1:
    print("Find world")
else:
    print("No World")

print("The %s ,weight is %d kg!" % ('World', 21))

TestString = """100==Standard,
 101==NonStandard"""

# print(TestString)

print("------------------")

TestString = TestString.replace("\n", "")
# print(TestString.split(","))

for block in TestString.split(","):
    matchObj = re.match( r'(.*)==(.*).*(?<!==)$', block)
    if matchObj:
        print(block.strip())


floatExample = 0.2234325
print("%.3f%%" % (floatExample/2))
print("%d" % (floatExample))
