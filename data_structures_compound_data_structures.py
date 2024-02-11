# Compound data structures - data structures/containers containing data structures

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

print(elements["helium"])
print(elements["hydrogen"]["weight"])

# Add new key to the dictionary
oxygen = {"number":8,"weight":15.999,"symbol":"O"}
elements["oxygen"] = oxygen
print(elements)

# EXAMPLE 2
print("\n EXAMPLE 2 \n")

student_records = {
    'John': {
        'age': 20,
        'major': 'Computer Science',
        'grades': [85, 90, 92]
    },
    'Emma': {
        'age': 19,
        'major': 'Mathematics',
        'grades': [95, 88, 91]
    }
}

# Add a new student_records
student_records['Alex'] = {
    'age': 21,
    'major': 'Physics',
    'grades': [80, 85, 88]
}

# Append new grade
student_records['John']['grades'].append(88)
print(student_records)