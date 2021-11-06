import numpy as np
lst=[1,2,3,4,5,6,7,8,9,10] 
arr=np.array(lst)
# print(arr)
# adding one to each element
# print(arr+1)

# property that determines the dimension of the array
arr.ndim 
# how many elements are there and the dimension
# print(arr.shape)

# another way of creating np array       
new_arr=np.arange(3,11)
# print(new_arr)
# we can also give step size

# special arrays in numpy 
np.zeros((4,4))     
np.ones((5,5))
np.diag([1,2,34,5])
np.identity(4) # identity matrix

# indexing in array
# creating a random array
array=np.random.randint(10, 100)
matrix=np.random.randint(1, 100,(5,4))
# print(matrix)
# print(matrix[4,3])
# slicing
new_matrix=matrix[2:5,1:]
# print(new_matrix)

# third column only
# print(matrix[:,2])

#check if elements greater that 10 
mask=matrix>10
# print(mask)
# print(np.sum(mask))

# get all elements greater than 10 
# print(matrix[mask])

# put multiple values equal to  zero 
matrix[2:,2:]=0
# print(matrix)

# basic operations in array

a=np.array([10,20,30,40])
b=np.arange(1,5)
# element opers
# print(a+b)
# print(a-b) 
# print(a*b)
b**2
np.log(b)
np.sin(b)

# multiplying two matrices 
A=np.random.randint(0,5,(3,4))
B=np.random.randint(0,5,(4,2))
C=np.dot(A,B)
# print(C)

D=np.arange(0,24)
# print(D)
D=D.reshape(6,4)
# print(D)

np.sqrt(D)
np.sum(D)
np.max(D)
# mean of elements
np.mean(D)
# standard deviation of elements
np.std(D)

# row wise sum of elements
# print(A)
# column wise sum
# print(np.sum(A,axis=0))
# row wise sum 
# print(np.sum(A, axis=1))

# Shape manipulation
D=D.reshape(6,4)
D=D.flatten()
# print(D)
# print(A)
# print(A.T)
# np.transpose(A)

# stacking of arrays-horizontal and vertical 
E=np.random.randint(0,10,(2,2)) 
F=np.random.randint(0,10,(2,2))

print(np.hstack((E,F)))
print(np.vstack((E,F)))

#vectorization
p1=np.array([1,2,4,7])
p2=np.array([5,5,8,2])

s=0
for i in range(4): 
    s+=(p2[i]-p1[i])**2
print(s**0.5)

np.sqrt(np.sum((p2-p2)**2)) 