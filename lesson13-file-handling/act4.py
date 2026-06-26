file = open("readme.txt", "r")
lines = file.readlines()
file.close()

outfile = open("append.txt", "a")
for line in lines:
    outfile.write('\n' + line)
