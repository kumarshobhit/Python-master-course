# print("Hello World") 
n=7
# print(n)
type(n)
# print(type(n))
s="Hey"
# print(s)
# print(type(s))

age=5
# if(age>=18): 
#     print("you are eligible")
# elif (age<12):
#     print("Go home kid")
# else:
#     print("Grow up Fast")

i=0
while(i<=10):
    # print(i,end=" ")
    i+=1 

# takes a starting and ending point but ending point is not included
# for k in range(5,20): 
    # print(k)

# step to increment/decrement
# for k in range(5,20,3):
    # print(k)

# name=input("enter your name") 
# print(name)
# typecasting the inputs

# Functions
# return_type func_name(params){
#     ...
#     return something
# }

def greeter(name):
    print("Hello "+name)
    print("I am enjoying Python.")
    return 5+5+6
    
# greeter("shobhit")

def is_even(no):
    if(no%2==0):
        return True
    else:
        return False
    
# print(is_even(15))

def is_prime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
    return True 

print(is_prime(23))

# Higher Order Functions
# First Class Objects

# Data Structures in Pyhon
# from typing import List
# 1.List 
# 2.tuples 
# 3.set 
# 4.dictionary

# List in python are heterogeneous
li=[5,2,9,10,56,23]
# print(type(li))
# print(li[0])
# #  negative indexing
# print(li[-2]) 

# # list slicing 
# print(li[1:5])
# print(li[:5])
# print(li[-6:2])
# print(li[-1:-6:-1])

li.append(100)
# print(li)
li.sort()
# print(li)
li.sort(reverse=True)
# print(li)
li.insert(2,999)
# print(li)
li.remove(999)
# print(li)


li2=[5,2,9,10,'Hello World,',True,6.5,9.0,[1,2,3],33,11]
# print(li2)
# for ele in li2:
    # print(type(ele))
    # print(ele)

# li2[0]=50

# converts list into tuple
# tuple(li2)
# converts tuple into list
# list(tup)

# list comprehension in python

# tuples
# tuples are read only you cannot change values
# tuples are immutable
tup=(1,2,3,4,5)
# print(type(tup))
# tuples are faster than list

# set
# only contains unique elements
s={1,2,3,4,5,6}
# print(type(s))
# sets are not subscriptable
# indexing is not possible
# print(s[0])- error

s1={1,2,3,4,5}
s2={8,4,3,5,10,13}

s1.intersection(s2)
s1.union(s2)
s1.add(999)

# Dictionary
# used as a HashMap
# stores data in key value pairs
# access time is O(1)

food_menu={'samosa':10,'burger':25}
print(type(food_menu))
# print(food_menu)
# print(food_menu['burger'])
# if the item is not present then there will be key error
# print(food_menu['pizza']) 
food_menu['pizza']=100
# using get method will give -1 if item is not there
# print(food_menu.get('pizza'))
food_menu['juice']=[20,40,60]
food_menu['fruits']={'apple':20,'mango':25,'kiwi':50}
print(food_menu)
print(food_menu['juice'][0])
print(food_menu['fruits']['kiwi'])
# integer interning
# string interning


