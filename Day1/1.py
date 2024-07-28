#print 
print("hlw")


# variables 
myFvrt= "penguin love"
print(myFvrt)

# Camel Case
# Each word, except the first, starts with a capital letter

myFvrt= "penguin love"
print(myFvrt)

# Pascal Case
# Each word starts with a capital letter

MyFvrt="penguins love"
print(MyFvrt)

# Snake Case
# Each word is separated by an underscore character
my_fvrt="penguin" 
print(my_fvrt)

# some variable assigns multipule valus 

x, y, z = "kona ", "limon", "nadus"

print(z,y)
print(x,y)
print(x,y,z)  

# k , m , t ="kona" 

# print(k , m , t ) not works 

k=m =t ="kona"
print (k,m,t)

# unpined list

biriany = ["rice", "beef ", "poteto", "botboti"]

x, y,z,k  = biriany
# x, y,z,k ,m = biriany
print(x) # rice 
print(y)   #beef
# print(m) # it will be error (expected 5, got 4)


x="i am tanisha"
print(x)

x=5
y="tanisha"
print(x,y) # when num and str together not work print (x+y). when both sathe and all same oparetor then it works with (+)


# global variables  
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x ="foolish girl"

def myFoolish():
    print(" i am the " , x) 
    
    
print(x)
myFoolish()
    
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

x = "kona"

def myfunc():
  x = "masud"
  print("Python is " + x)

myfunc()

print("Python is foolish " + x)

#  a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "ttttt"

myfunc()

print("Python is " + x)