def greetings(name): 
    return "Hello"+name

# print("I am inside a module called my_custom")

print("Imported module: ", __name__)

if(__name__=='__main__'):  
    print("I am very confidential") 
