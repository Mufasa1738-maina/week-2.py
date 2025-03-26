# create an empty list
my_list = []

# append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert the value 15 into position two
my_list.insert(1, 15)

# Extend my_list with another list
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

# sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is: {index_of_30}")

# Print the final state of my_list
print("Final state of my_list:", my_list)
