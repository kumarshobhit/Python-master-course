# function defination
def greetings(name):  
    print("Good morning",name)
greetings("Shobhit")

def add(a,b): 
    """ 
    this is a doc string 
    return sum of 2 numbers
    """
    return a+b

add(5,3)

# Functions can return multiple values in the form of a tuple
def calculator(a,b): 
    return (a+b,a-b,a*b,a/b) 
cal_res=calculator(6,4)
print(cal_res)

# arguments and parameters
# always write non default arguments first 
def intro(name,nationality='Indian'): 
    print("Hello",name)  
    print("I am",nationality)

intro("Shobhit","German")

# arbitrary arguments- it can get any number of arguments
# store in the form of a tuple
def random_func(*args): 
    print(args) 
    print(type(args))
random_func(1,2,3,4,5)

# keyword arguments-stores in the form of a dictionalry 
def introduction(**kwargs):
    print(kwargs) 
    print(type(kwargs))

    for(k,v) in kwargs.items():
        print(k," , ",v)

introduction(name='Shobhit',age=21,hobby=['coding','badminton'],nationality='Indian')

#inbuilt Functions
abs(-5.5)
round(5.679,2) # 5.68
round(5.789) # 6 will be printed

lst=[1,2,3,4]
sum(lst)
max(lst)
min(lst)

# map function
def add_one(x): 
    return x+1
map_ele=map(add_one,lst)
print(list(map_ele))

# filter function 
def is_even(x): 
    return x%2==0

filter_ele=filter(is_even,lst)
print(list(filter_ele))