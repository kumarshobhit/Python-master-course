age=21;
if(age>=18):
    print("you are eligible to vote");
    print("I am inside if block")
else:
    print("grow up");
print("I am inside else");
# indentation in python
num=4;
if (num>0):
    print("positive number");
elif(num==0):
    print("neutral number");
else: 
    print("negative number");

if (num >= 0):
    if(num==0):
        print("Zero");
    else: 
        print("positive number");
else:
    print("negative number");
 
# largest of three numbers
a,b,c=10,50,30;
if(a>b and a>c):  
    print(a);
elif(b>a and b>c): 
    print(b);
else: 
    print(c);

# while loop
i=1;
while(i<=20): 
    print(i,end=", ");
    i=i+1;
print();

# for loop
# end pos is not included 
for ele in range(3,13): 
    print(ele,end=", ");
    ele+=1;
print();

for ele in range(2,21): 
    if(ele%2==0): 
        print(ele,end=", ");
else: 
    print(); 
    print("No elements left");

# range function has step size 
for ele in range(2,21,2): 
    print(ele,end=", ");

print();
n=7;
for i in range(1,11): 
    print("{} X {} = {}".format(n,i,n*i));
else: 
    print("All done");

# pattern printing
# *
# ** 
# *** 
# ****  
# *****   
n=5;
# for i in range(1,n+1): 
#     for(j) in range(1,i+1): 
#         print("*",end="");
#     print();
# print("hello"*3);
# for i in range(1,n+1): 
#     print("*"*i);
# *****  
# ****  
# ***     
# ** 
# * 
# for i in range(n,0,-1): 
#     print("*"*i);

# Questions
# calculate sum of first n numbers
s=0
for i in range(1,n+1): 
    s+=i;
    i+=1;
print(s);

# you cannot keep a block as empty 
if(4<6): 
    pass

