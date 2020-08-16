#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
list
"""
p = (4, 5)
x, y = p
# x, y, z = p
#Exception has occurred: ValueError
#ValueError: not enough values to unpack (expected 3, got 2)
print(x, '\n', y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)
print(date)
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)


