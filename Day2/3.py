# Slicing string 

p="today is a rainy day"
print(p[2:6])   #position 6"i" not included 

# today is
# 0123456

print(p[:7])   # 0 to 7 positions , 7 not included in run 'today i'

print(p[2:])   # position 2 to end slow all , 2 included   'day is a rainy day'

# Negative Indexing

print(p[-5:-1])  #count from the last position is 0 .. and go right to left 'y da' 



# modify string 

myfvrt= " we are not rajakar "
killed=200
bullet=3
print(myfvrt.upper())
print(myfvrt.lower())
print(myfvrt.split())  
print(myfvrt.replace("rajakar", "hanadar"))

#  WE ARE NOT RAJAKAR
#  we are not rajakar
# ['we', 'are', 'not', 'rajakar']
#  we are not hanadar


# To specify a string as an f-string, simply put an f in front of the string literal,
# and add curly brackets {} as placeholders for variables and other operations.
txt=f"they killer {killed} peoples with {bullet:.2f} "
print(txt)

# escape String 

myfvrt= " we are not \"rajakar\" anymore "  #for using cotations 
print(myfvrt)


# Code	Result	Try it
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value




