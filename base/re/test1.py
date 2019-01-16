#!/usr/bin/env python
# Filename: test1.py
# -*- coding: utf-8 -*-

import re

print(re.match('www', 'www.google.com.cn').span())

Line = "Cat are smarter than dogs"
MatchObj = re.match( r'(.*) are (.*?) .*', Line, re.M|re.I )

if MatchObj:
    print("group()", MatchObj.group())
    print("group(0)", MatchObj.group(0))
    print("group  ", MatchObj)
    print("group(1)", MatchObj.group(1))
    print("group(2)", MatchObj.group(2))
    # print("group(3) error", MatchObj.group(3))
else:
    print("no match")
