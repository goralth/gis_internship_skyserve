# Creating a list, dictionary, and set
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2, "c": 3}
my_set = {1, 2, 3}

# Operations on the list
print("Original list:", my_list)
my_list.append(4)  # Adding an element
print("List after adding 4:", my_list)
my_list.remove(2)  # Removing an element
print("List after removing 2:", my_list)
my_list[1] = 5  # Modifying an element
print("List after modifying index 1:", my_list)

# Operations on the dictionary
print("\nOriginal dictionary:", my_dict)
my_dict["d"] = 4  # Adding a new key-value pair
print("Dictionary after adding key 'd':", my_dict)
del my_dict["b"]  # Removing a key-value pair
print("Dictionary after removing key 'b':", my_dict)
my_dict["a"] = 10  # Modifying a value
print("Dictionary after modifying key 'a':", my_dict)

# Operations on the set
print("\nOriginal set:", my_set)
my_set.add(4)  # Adding an element
print("Set after adding 4:", my_set)
my_set.remove(2)  # Removing an element
print("Set after removing 2:", my_set)
my_set.update([5, 6])  # Adding multiple elements
print("Set after adding 5 and 6:", my_set)

# Final results
print("\nFinal List:", my_list)
print("Final Dictionary:", my_dict)
print("Final Set:", my_set)
