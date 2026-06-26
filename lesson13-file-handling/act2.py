#skip lines 
word = input("Skip lines starting with : ")
file = open("readme.txt", "r")

lines = file.readlines()
for line in lines:
    if line.startswith(word):
        continue
    else:
        print(line.strip())
file.close()