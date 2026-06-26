file = open("readme.txt", "r")
todos = file.readlines()

print(todos)
print('--------------- CONTENT ---------------')
print('\n')

for index, todo in enumerate(todos, start = 1):
    print(f"{index} - {todo}")
#Reading only first 11 characters
file.seek(0)
print("\nPrint First 11 characters only from the file : ")

print(file.read(11))

file.close