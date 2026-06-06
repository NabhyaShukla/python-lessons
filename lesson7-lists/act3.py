# Convert List to a dictionary
roll_numbers = [1,2,3,4,5]
names = ["Nabhya", "Ishant", "Nawanjeet", "Mohandas Karamchanda Gandhi", "Shubhash Chandra Bose"]


st_dict = dict(zip(roll_numbers, names))
print(st_dict)

for key, val in st_dict.items():
    print(f"{key} : {val}")


