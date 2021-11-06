my_str="hello how are you"
# total number of characters in a string
print(len(my_str))
# accessing last elemenent        
print(my_str[len(my_str) - 1]) 
# negative indexing   
print(my_str[-1]) ; # last character  
print(my_str[-5]) ; # 5th last character 
# string slicing  
# start and end+1
print(my_str[2:7]) ;
#print whole string
print(my_str[:])
# only the last two characters are left      
print(my_str[:-2]) ;
#lowercase  
print(my_str.lower()) 
#uppercase
print(my_str.upper()) 
# Capital first character of each word 
print(my_str.title()) 
# return the index of the first occurrence of the word 
print(my_str.find("how"))
print(my_str.find("hoo"))
# splits the string with space " " and creates a list      
list=my_str.split(" ")
print(list)
# repeat a number n no of times
print("hello "*5)

# lists in python
my_list=[5,6,7,8,9]
# add element at the end of list
my_list.append(33)
# inserts 88 at index i  at which index you want to insert             
my_list.insert(1,88) 
# delete the last element                                             
# pop function can also take an index if you want to delete at an specefic index 
my_list.pop()
# reverse a list   
my_list.reverse()
# sorts in ascending order  
my_list.sort()
# descending order 
my_list.sort(reverse=True)
# in operator  
8 in my_list

# list comprehension
new_list=[] 
for ele in my_list:   
    new_list.append(ele**2) 

new_list2=[ele**2 for ele in my_list] 

# tuples are similar to a list but you cannot change elements inside a tuple
tup=(8,9,'Hello',88) 

# set contains only unique elements
my_set={9,7,7,1,8,9,7,5,1}
# no duplicate elements 
print(my_set)
# add elements
my_set.add(99)
# remove element 
my_set.remove(8)

some_list=[6,3,3,8,3,4,5,9]
my_new_set=set(some_list)
# some_list=list(my_new_set)

# dictionaries
user_info={
    "name":"Shobhit",
    "age":21,
    "nationality":"Indian"
}

# to get value of key
user_info.get("hobby")
# display all keys in dictionary
user_info.keys()
# display all values in dictionary  
user_info.values() 
# display {key,value} pair in tuples 
user_info.items() 
# iterate over a list 
for(k,v) in user_info.items():  
    print(k," : ",v)
# delete key   
user_info.pop('nationality')


lst1 = [2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]

result = lst1 + lst2
print(result)

newList=[i**2 if i%2==0 else i**3 for i in range(0,len(lst1))]

a = [1, 5, 3, 2, 4, 3, 2]
b = [5, 3, 4, 2, 1]

print(set(a) == set(b))
