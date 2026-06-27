L = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

"""
Write a function to find the items with unique values
Output : 
    Unique values : {'S009'}, {'S002'}, {'S007'}, {'S005'}, {'S001'}
"""

unique_vals = set() #empty....set always store unique values
for double in L:
    unique_vals.update(double.values())

print(unique_vals)