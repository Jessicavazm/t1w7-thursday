# Creating a dictionary, "name" = key and "Jessica" = value
my_dict = {
    "name": "Jessica",
    "age": 30,
    "city": "Melbourne"
}
print(my_dict)

# Access the values by keys
print(my_dict["name"])
print(my_dict["city"])

# Adding a new key-pair value
my_dict["email"] = "jessv@example.com"
print(my_dict)

# Adding an item with an existing key overwrites the original value
my_dict["city"] = "Sydney"
print(my_dict)

# Removing a key-value pair
del my_dict["age"]
print(my_dict)

print("-----")
# Alternatively, you can use .pop() to remove, here you use small brackets because .pop is a method -> pre defined function, to use the function you need to call it by using dot.
my_dict.pop("email")
print(my_dict)

# Check for a key existence
print("email" in my_dict)

# Trying to find the key using a value, you have to extract the keys and values to variables and extract them as a list. Then you can use index of value to find the key.
list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())

print(list_of_values.index("Jessica"))
print(list_of_keys[0])

# Interate through dictionary, key and value after the for are variables. 
# .item gets each item inside of the dictionary
for key, value in my_dict.items():
    print(f"{key}, {value}")

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Jess", "age": 30},
    "person2": {"name": "Luke", "age": 42}
}

print(nested_dict["person2"]["name"])


# Merging Dictionaries using | <-- straight line
merged_dict = my_dict | nested_dict
print(merged_dict)