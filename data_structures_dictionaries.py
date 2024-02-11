# Dictionary - A mutable data type/DS that stores mappings of unique keys to values
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])

# Memberships
print("carbon" in elements)

# GET - returns None if key is missing
print(elements.get("Boron"))

# Identity
result = elements.get("oxygen")
print(result is None)
print(result is not None)