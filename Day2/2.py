x=10E2
print (type(x))

x=10e2  #e is power
print (type(x))

x=4
y=5.8
z=1+4j

# conver x in float

x=float(x)
print(x)

# convert x in complex 
x=complex(x)
print(x)

# random function
import random
print(random.randrange(1,10))  #give any number in range (1 to 10)

# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# float
x=float("3.4")
y=float(3.4)
z=float(3)
p=float('3.4')
print(x,y,z,p)


# str 

x=str("3.4")
y=str(3.4)
z=str(3)
p=str('3.4')
print(x,y,z,p)

# string 
x ="kona"
print(x)

# multy lines for  """   or '''

a="""fbhdfaksrek
bvdsbfhesg
dsjbhsgbhea
ndsjbghsbg
"""
print(a)
print(a[1])   #count start from 0 
print(len(a))
#  loop string 
for a in "alu vorta":
    print(a) 
      
      
      
# To check if a certain phrase or character is present in a string, we can use the keyword in.
x=" hi i am tunir nani"
print("nani" in x)   # if nani is found then return true ,else false

tut=" hi i am tunir nani"
print("nana" not in tut)  # it run true . bcz of not oparetor


p=" ajk kotha hobe na " 
if "kotha" in p :
    print("ok")
else:
    print("not ok")








