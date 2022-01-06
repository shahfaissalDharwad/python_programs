#creating an emppty set
b = set()
print(type(b))

#adding values to empty set

b.add(4)
b.add(5)
b.add((4,5,6)) # CAN ADD TUPLES BUT CANNOT ADD DICT AND LIST TO SET
print(b)
# print length of the set
print(len(b))

# removal of an item
b.remove(5) # removes 5
#b.remove(15) # throws an error while trying to remove (which is not in the set)
print(b)

print(b.pop())
print(b)