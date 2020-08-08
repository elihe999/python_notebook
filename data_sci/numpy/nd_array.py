# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import numpy as np

data = [1, 2, 3, 4]
arr = np.array(data)
print(arr)

data1 = [data, data]
arr1 = np.array(data1)
print(arr1)

# create array : zero
print(np.zeros((3, 3)))
# create array : ones
print(np.ones((3, 3)))

#arithmetic
print(np.arange(1, 10, 2))
#
print(np.linspace(1, 10, 4))

#data type
arr2 = np.array([1, 2, 3, 4])
print(arr2.dtype)
