#creating an account
name = input("please enter your name: ")
surname = input("please enter your surname: ")
age = input("please enter your age: ")
gmail = input("please enter your gmail: ")
print(f"your name is {name}. your surname is {surname}. your age is {age}. and lastly your gmail is {gmail}.")
fullname = name + " " + surname
print(f"thank you for signing up {fullname} we will notify you on your gmail {gmail} if there are any suspicios activities on your account")

#numbers

num1 = int(input("please enter a number: "))
num2 = int(input("please enter a second number: "))
num3 = int(input("please enter a third number: "))

print(num1 + num2 + num3)
print(num2 - num1 + num3)
print(num3 / num1)
print(num1 * num2 + num3)
print(num1 + num2 * num3)
print(num3 / num2 + num1 + num3)

#items cost and the number of items

cost = int(input("this item costs: "))
quantity = int(input("how many do you want to buy: "))
total_cost = int(cost * quantity)
input(f"the total cost will be {total_cost}")

