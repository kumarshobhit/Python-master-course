# import math
import random
from math import gcd
import os
import my_custom
# print(dir(math))
# print(gcd(4,8))
# ans=random.random()
# print(ans)
# print(os.getcwd())

print("main file: ", __name__)


def func(lst):
    lst.extend([5, 6, 7])


l = [1, 2, 3, 4]
func(l)
print(len(l))

marks=[1,2,3,4,5,6,7,10,8,9]
sorted_marks=sorted(marks)
print(sorted_marks)
dic={}
for i in marks:
    if i in dic.keys():
        dic[i]+=1
    else:  
        dic[i]=1
