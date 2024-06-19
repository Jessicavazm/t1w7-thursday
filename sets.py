# Creating a set
my_set = {1, 2, 3, 4, "apple"}

print(my_set)

# Adding an element
my_set.add(5)
print(my_set)

# Removing an element
my_set.remove("apple")
print(my_set)

# Membership testing
print(6 in my_set) # False
print(4 in my_set) # True

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("-------")
# Union
union_value = set_a.union(set_b)
print(union_value)

# Intersection
intersection_value = set_a.intersection(set_b)
print(intersection_value)

# Difference
difference_value = set_a.difference(set_b)
print(difference_value)