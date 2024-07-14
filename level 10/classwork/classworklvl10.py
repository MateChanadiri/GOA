age = int(input("how old are you: "))
if age < 13:
    print("pipsquek")
elif age > 14:
    print("yo we got a big fella here")
else:
    print("your not more than 50... right? you CANT be right?")


house_temp = 31
if house_temp > 30:
    print(f"Detected temperature {house_temp}, your ac is turning on Matthew")



for i in range(101):
    print(i)

for i in range(1, 11, 2): 
    print(i)

for i in range(100, 1, -1):
    print(i)

counter = 0
while counter < 101:
    print(counter)
    counter = counter + 1

counter = 0
while counter < 11:
    print(counter)
    counter = counter + 2

counter = 101
while counter > 0:
    print(counter)
    counter = counter - 1

i = 300
while i > 0:
  print(i)
  i = i - 1

counter = 0
while counter < 4:
  print(counter)
