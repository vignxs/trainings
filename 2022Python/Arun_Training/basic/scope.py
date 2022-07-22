x=10; 
def fun():
    global x
    x = 17  
    print("local var" ,x)
fun();
print("globale var" ,x)


#Globale and local in same fun 

x=10; 
def fun():
    x = 17
    print(id(x))  
    print("local var" ,x)
    globals() ['x'] = 19
fun();
print(id(x))  
print("globale var" ,x)


