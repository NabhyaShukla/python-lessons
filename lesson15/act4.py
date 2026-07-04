import os
import time
if os.path.exists('appended.txt'):
    print("File exists")

    choice = input("Do you want to remove this file? (y/n) : ")
    if choice in ['yes', 'yeah', 'yea', 'remove', 'remove it', 'y']:
        os.remove('appended.txt')
        time.sleep(2)
        print("File removed successfully...")
    else:
        print("Ok, just one more thing...\n")

    choice2 = input("Do you want to create a new file 'wow.txt'? [y/n] : ")
    if choice2 in ['yes', 'y']:
        open("wow.txt", 'w')
    else:
        print("Fine then, HAPPY SEARCHING!")

    
else:
    print("File 'appended.txt' doesnt exists")
    choice2 = input("Do you want to create a new file 'appended.txt'? [y/n] : ")
    if choice2 in ['yes', 'y']:
        open("appended.txt", 'w')
        print("File has been APPEARED...")
    else:
        print("Fine then, HAPPY SEARCHING!")
