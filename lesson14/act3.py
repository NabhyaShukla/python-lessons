#Checking before merging
import os 
if os.path.exists("dummy.txt"):
    print("File already EXISTS...")
else:
    print("File not present")

content = '' #empty string

#stored content of first file
with open('class_notes.txt', 'r') as f1:
    content += "This is first file, 'class_notes.txt'\n"
    content += "="*49
    content += '\n' +f1.read() + '\n'

#stored content of secodn file
with open('smthng.txt', 'r') as f2:
    content += "\nThis is second File, 'smthng.txt'\n"
    content += "="*49
    content += '\n' +f2.read() + '\n'

#write both in third file
with open('dummy.txt', 'w') as out:
    out.write(content)
print("Saved all data to 'dummy.txt'...")

