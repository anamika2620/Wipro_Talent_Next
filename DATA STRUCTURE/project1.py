
# Dictionary of people and their interesting facts
people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original dictionary
print("Original List:")
for name, fact in people.items():
    print(name + ":", fact)

# Change a fact about one person
people["Jeff"] = "Is afraid of heights."

# Add a new person and fact
people["Jill"] = "Can hula dance."

# Display updated dictionary
print("\nUpdated List:")
for name, fact in people.items():
    print(name + ":", fact)
