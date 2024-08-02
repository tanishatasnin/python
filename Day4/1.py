# x=input("Enter first value : ")
# y=input("Enter second value: ")
# print(x-y)



# tuple  

myFnds = ("limon", "anik", "masud", "masud" , "masud", 12, 12 , 0 , 3 )
myZone=["limon", "anik", "masud", "masud" , "masud", 12, 12 , 0 , 3 ]

print(myFnds)  #Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 

print(myZone)    #List is a collection which is ordered and changeable. Allows duplicate members.


# convert 
x = ("apple", "banana", "cherry")
y = list(x)

print(y)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Convert the tuple into a list, add "orange", and convert it back into a tuple 
x = ("apple", "banana", "cherry","mango")
y=list(x)
print(x)

y.append("pinapple")
x=tuple(y)
print(x)


# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# f the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, * yellow, red) = fruits

print(green)
print(yellow)
print(red)