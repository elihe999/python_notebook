import numpy as np

a=np.array([1,2,3,4])
print(a)
print(a.dtype)
#type of array
#np.array(1,2,3,4) wrong
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)

b=np.array([[1,2,3],[4,5,6]],dtype=complex)
print(b)
print(b.dtype)

c=np.zeros((3,3,3))
print(c)

c=np.ones([3,3],dtype=int)
print(c)
c=np.empty([2,3,3])
print(c)
c=np.arange(6)
print(c)

