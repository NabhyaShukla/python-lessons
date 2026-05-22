import datetime
import calendar

#  using now() to get current time
current_time = datetime.datetime.now()

# Printing the current time
print("Time now at Greenwich meridian is : ", current_time)

# User choice
print("\n1. Show whole year calendar")
print("\n2. Show single month calendar")

choice = int(input("\nEnter your choice [1/2] : "))

if choice == 1:
    year = int(input("\nEnter Year : "))

    # print whole year calendar
    print("\n")
    print(calendar.calendar(year))

elif choice == 2 :
    year = int(input("Enter Year : "))
    month = int(input("Enter Month (1-12) : "))

    #print single month calendar
    print("\n")
    print(calendar.month(year, month))

else:
    print("Invalid Choice!")

