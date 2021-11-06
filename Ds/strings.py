# in strings for indexing space are also counted
s="Welcome to the course";
print(len(s));
# negative indexing
print(s[-1]);
print(s[-5]);

# string slicing
print(s[0:7]);
# print all the characters except the last one
print(s[0:-1]);
print(s[:]);
# step size
print(s[0:7:2]);
# backward direction
print(s[20:5:-1]);
# reverse a string
print(s[::-1]);