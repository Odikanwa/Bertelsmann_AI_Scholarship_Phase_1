import time
# Set - A DS for mutable unordered collection of unique elements. Set operations are faster than list operations
months = ["Jan", "Feb", "Mar", "April", "May", "Mar", "Apr", "Dec", "Oct", "Jan", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
week_days = {"Mon", "Tue", "Wed", "Thur", "Fri"}
# Create a set from a list
print(set(months))

# Membership
print("Thurs" in week_days)

# ADD - Adds a new element randomly
week_days.add("Sat")
print(week_days)

# POP - Reemove a new element randomly
week_days.pop()
print(week_days)

# Union, Intersection & Difference


# Sample data
set1 = set(range(10))
set2 = set(range(5, 15))
list1 = list(set1)
list2 = list(set2)

# UNION
union_set = set1.union(set2)
print("Set: \n", union_set)

# convert to a list
union_list = list(set(list1 + list2))
print("list: \n", union_list)

# INTERSECTION
intersection_set = set1.intersection(set2)
print("Intection in Sets: \n", intersection_set)

# Intersection in List
intersection_list = [x for x in list1 if x in set2]
print( "Intersection in List:\n", intersection_list)

# DIFFERENCE in Sets
difference_set = set1.difference(set2)
print("Difference in Sets: \n", difference_set)

# Difference in Lists
difference_list = [x for x in list1 if x not in set2]
print("Differenece in Lists: \n", difference_list)


