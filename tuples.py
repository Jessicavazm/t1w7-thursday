# Creating a tuple
my_tuple = (1, 2, 3, "a", "happy")

# Accessing elements with index, elements can't be changed in tuples.
print(my_tuple[3])


# Tuples can be unpacked, you just need to define variables first and then assign them to tuple.
a, b, c, d, e = my_tuple
print(a, e)

# Tuples can contain other tuples (nested tuples)
nested_tuple = (1, (2,3), (4,5), (0,0))
print(nested_tuple[1][1])
