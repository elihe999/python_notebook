#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

testStr="100==Standard"

matchObj= re.match( r'(.*)==(.*).*(?<!==)$', testStr)
if matchObj:
    testArray=testStr.split("==")
    print(testArray)
    for subArr in testArray:
        matchNumber = re.match(r'^\d+$', subArr)
        if matchNumber:
            print(subArr)
        matchNonFormNumber = re.match(r'^(0|[1-9][0-9]*)$', subArr)
        if matchNonFormNumber:
            print(subArr)

