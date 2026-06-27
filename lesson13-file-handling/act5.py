"""

    READ ALL THE NAMES LINE-BY-LINE AND STORE ONLY THOSE NAMES
    IN ANOTHER LIST , WHERE THE LENGTH OF NAMES ARE GREATER THAN 4 
    AND PRINT IN ANOTHER FILE 'WORDS_OUT.TXT'

"""
# input_file = open('word.txt', 'r')
# output_file = open('words_out.txt', 'w')

# for line in input_file:

#     name = line.strip()
#     if len(name) > 4:
#         output_file.write(name + '\n')

# input_file.close()
# output_file.close()

long_name =[]

file = open('word.txt', 'r')
names = file.readlines()
for name in names:
    clean_name = name.strip()

    if not clean_name:
        continue

if len(clean_name) > 4:
    long_name.append(clean_name)

file.close()

output_file = open('outfile.txt', 'w')
for name in long_name:
    output_file.write(name + '\n')

output_file.close()
print("Done....")