myList = []
print(myList)

# List of Numbers
myList2 = [100, 5, 25.5, 17, 2, 900]

# List operations
# Append() = adds an element to the end of the list
print(myList2)
myList2.append('45')
print(myList2)

# Pop() = removes the last element from the list
popped_item = myList2.pop()
print(popped_item)
print(myList2)

# sort() = sorts the list in ascending order
myList2.sort()
print(myList2)

# Remove() = removes the first occurrence of a specified value from the list
search_item = 25.5
if search_item in myList2:
    myList2.remove(search_item)
    print(f"{search_item} has been removed from the list.")
else:
    print(f"{search_item} not found in the list.")

print(myList2)

# reverse() = reverses the order of the list
myList2.reverse()
print(myList2)

# loop through a list
for item in myList2:
    print(item)

# clear() = removes all the contents from the list
myList2.clear()
print(myList2)

# delete() = deletes the list and variable permanently
del myList2
