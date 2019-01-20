#!/usr/bin/python3
# -*- coding: utf-8 -*-

*trailing, current = [10, 9, 8, 7, 6, 5, 3]
print(trailing)
print(current)

recode = ('ACME', 50, 123.32, (12, 18, 2012))
name, *_, (*_, year) = recode
print(name)
print(year)
# print(_)