file = open("readme.txt", "r")
lines = file.readlines()
file.close()

outfile = open('oddLines.txt', 'w')

for i in range(0, len(lines), 2):
    outfile.write(lines[i])

outfile.close()
print("Odd lines are saved in outfile.txt")
