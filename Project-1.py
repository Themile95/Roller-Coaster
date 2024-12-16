print("Welcome to the rollercoaster!!!")

height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What Is Your Age? "))
    if age < 12:
        bill = 5
        print("Child Tickets Are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets Are $7.")
    else:
        bill = 12
        print("Adult Tickets Are $12.")
    photo = input("Do You Want Your Photo? Y or N. ")
    if photo == "y":
        bill += 3
    print(f"Your Final Bill Is ${bill}.")
else:
    print("You Can't Ride The Rollercoaster.")

