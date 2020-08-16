
#sort
#search

import numpy as np

s = np.array([1,2,3,4,5,4,3,2,1,2,34,5,6,7])
print( np.sort(s) )
print( np.argsort(s) )
print( np.array(sorted(s, reverse=True)) )

arr1 = np.array([[0,1,3],[4,2,9], [4,5,6], [1,-3,2]])
print( np.sort(arr1, axis=1))

#where
print( np.where(s>3,1,-1) )
print( np.where(s>3,s,-1) )

