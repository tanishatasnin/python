x=["kona", "masud" ,"limon"]   #list
print(x)
print(x[2],x[0])
print(len(x))



#  diffrent data type can be togather in a list
y=[12, "kona", True]
print(y)
print(len(y))



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List--- is a collection which is ordered and changeable. Allows duplicate members.
# Tuple--- is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

x=["kona", "masud" ,"limon","nusrat","saida","anik", "jiku","ammar","nazmul","ononno","moeen"]

x[2:3]=["anika", "tuktuki"]   #['kona', 'masud', 'anika', 'tuktuki', 'nusrat', 'saida', 'anik', 'jiku', 'ammar', 'nazmul', 'ononno', 'moeen'] its modify
print(x)


x.insert(5,"mimi")  #need given index
print(x)

x.append("tuni")   # apend add in the last of the list
print(x)

z=["adnan", "tasin ", "musfiq"]

x.extend(z)   # add 2 list togather from the last
print(x)


# from delete (pop , del,remove ,clear )

x.remove("kona")

#  del (x)  # delete the list

x.pop(5) # pop saida

x.clear()
print(x)




