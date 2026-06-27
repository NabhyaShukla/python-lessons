import os
if os.path.exists("words.txt"):
    os.remove('words.txt')
    print("words.txt file deleted successfully...")
else:
    print("This file DOESN'T EXISTS")

#REMOVES THE FILE!!!!