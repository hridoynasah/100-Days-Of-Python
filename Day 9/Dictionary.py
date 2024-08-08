programming_dictionary = {
    "Bug": "A bug in programming is an error, flaw, or fault.",
    "Function": "A function in programming is a reusable block of code",
}
print(programming_dictionary["Bug"])

# Adding new items to dictionary: Because it is mutable
programming_dictionary[123] = "This is a number."
print(programming_dictionary)

# Empty Dictionary:
empty_dictionary = {}

# Wipe an existing dictionary:
# programming_dictionary = {}
# print(f"This dictionary is empty now {programming_dictionary}.")

# Edit an item in a dictionary:
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Loop through a dictionary: key
for key in programming_dictionary:
    print(key)
# Loop through a dictionary: value
for key in programming_dictionary:
    print(programming_dictionary[key])


