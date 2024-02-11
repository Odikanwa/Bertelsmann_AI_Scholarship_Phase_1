# Data structures - containers for grouping datatypes together
# Types of Data structures - Lists, tuples, sets, dictionaries, compound data structures
# List - DS for mutable ordered sequence of elements

week_days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
# Get first item
print(week_days[0])
# Get Last item
print(week_days[-1])

# Get 3rd to 6th item
print(week_days[2:6]) #inclusive of 2 but exclusive of 6

# Get up to the 6th item
print(week_days[:6])

# Get from 3rd to last item
print(week_days[2:])

# Operations - Memberships & Identity
print("Wed" in week_days)
print("Flat" not in week_days)

# Mutability
week_days[3] = "Thur"
print(week_days)

# List Methods - len(), max(), min(), sorted(), join(), append

numbers = [0, 2, 8, 6 , 10, 4]
# SORTED - Sort by default - ascending
print(sorted(numbers))
# SORTED - Sort in reverse
print(sorted(numbers, reverse=True))
# JOIN - Join the days of the week
joined_weekdays = "\n".join(week_days) #Join by new line
print(joined_weekdays)
# APPEND - Add element to the end of the list
numbers.append(12)
print(numbers)