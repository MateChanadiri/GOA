#first work

age = int(input("enter your age: "))
if age < 18:
    print("You get a discount")
else:
    print("Regular price")

#second work

num = int(input("Enter your winning number: "))
if num == 6:
    print("You won a house")
elif num == 30:
    print("You won a hawai ticket")
else:
    print("you won a dollar")

#third work

age = int(input("Enter your age: "))
student = input("are you a student?: ")
if student == "yes":
    student = True
else:
    student = False

if age < 18 or student == True:
    print("You get a discount")
else:
    print("You dont get a discount")

