def greet(fname, lname):
    print(f"Hello Coder, {fname} {lname}!!")

greet("Jess", "Vaz")

# Using Keywords args

greet(fname="Jess", lname="Vaz")

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} called {pet_name}")

# Positional argument
describe_pet("Willie")

# Positional and default argument
describe_pet("Harry", "Hamster")

# Keyword Arguments
describe_pet(animal_type="cat", pet_name="Zack")