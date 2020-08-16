#!/usr/bin/env python3

"""
提供一个数组，按照一定的顺序排列起来 能有几种组合
"""
def permutations(arr, position, end):
 
    if position == end:
        print(arr)
 
    else:
        for index in range(position, end):
 
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
 
 
arr = ["a","b","c"]
permutations(arr, 0, len(arr))