#This is a comment
#This line will not be executed
print("hello students");
#You can print multiple objects 
print("Python","data science","master course");

#creating a variable
i=40;
#finds data type of variable
print(i);
type(i);
#gives location where variable is stored
print(id(i));
#Python is dynamic 
#same variables can take values of different data types
#all variables are objects in python

print(type(55.55));
my_c=4+3j;
print(type(my_c));

flag=False; #or True
print(type(flag));

print(type(None));

# name=input("enter your name ");
# print(name);
#typecasting change the datatype
num="8";
print(type(num));
num=int(num)
print(type(num));

# multi line statement
a=1+2+3+\
    4+5+\
        6+7;
print(a);

#Output formatting
a=10;
b=20;
print("The value of a is {} and b is {}".format(a,b)); #default
print("The value of b is {1} and is {0}".format(a,b)); #specify the position of arguments   
name="Shobhit";
greetings="Good morning";
print("Hello {n} ,{g}".format(n=name,g=greetings));

grade_1 = 25
grade_2 = 75
average = grade_1 + grade_2/grade_1 + grade_2/2
print(average)


# operators
# division which gives quotient as floor values
no1=12;
no2=3;
div=no1/no2;
print(div);
# floor division
div2=no1//no2;
print(div2);
# exp 
expo=no1**no2;
print(expo)

#logical operators
# and,or,not
print((105) and (5>10));

# bitwise operators
print(bin(48));

#special operators
# to check for a substring
my_str="Good morning";
print("Good" in my_str);
print("Bad" in my_str);

n1=5000
n2=300
# is will check the location
# == compares the value 
# print(n1 is n2);
# print(n1 is not n2);

print(2**(3**2));
print((2**3)**2);
print(2**3**2);
