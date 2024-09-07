#1
a = 5
b = 10

total = a + b

print(total)

#2
str1 = "Hello"
str2 = "World"

# Concatenate thae two strings which is merging a new string like Hello world by +
merged_str = str1 + " " + str2

print(merged_str)
#3
x = 7
y = 3

# a division operation whicha results in a float because 7 / 3 is 2.333333333333333333333333333...
result = x / y

print(result)
#4
# Explicitly convert an integedr to a float
x_float = float(x)

print(x_float)
#5
a = 10
b = 20

# Codsmparison operator exama sdples
print(a == b)
print(a != b) 
print(a > b)   
print(a < b)   
print(a >= b)  
print(a <= b)  
# 6
result_6 = (5 + 5 == 8 + 2)  
print(result_6)

# 7
# # A and B
# A or B
# not A
# not B
# not (A and B)
# not (A or B)
# A and not B
# A or not B

# 8
result_8_1 = (5 > 3) and (2 < 4)  # True because both conditions are true
result_8_2 = (5 == 5) or (10 < 5)  # True because at least one condition is true
result_8_3 = not (7 > 10)  # True because 7 is not greater than 10
result_8_4 = (4 <= 4) and not (2 == 3)  # True because both conditions are true
result_8_5 = (8 > 5) or (3 > 6)  # True because at least one condition is true

print(result_8_1)
print(result_8_2)
print(result_8_3)
print(result_8_4)
print(result_8_5)

# 9
for i in range(1, 11):
    print(i)

# 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_total = 0
for number in numbers:
    sum_total += number

print(sum_total)

# 11
text = "Hello, World!"
print("Characters:")
for char in text:
    print(char)

# 12

i = 1
while i <= 10:
    print(i)
    i += 1

# 13
print("1 to 100, skipping 50 to 60:")
for number in range(1, 101):
    if 50 <= number <= 60:
        continue
    print(number)

# 14
sum_total = 0
num = 1
while sum_total < 50:
    sum_total += num
    num += 1

print(sum_total)
print(num - 1)

# 15
def insert(number):
    if number % 3 == 0 or number % 5 == 0:
        print(number)
insert(6)
# 16
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
average()
# 17
def alternate_uppercase(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i].upper()
        else:
            result += s[i]
    return result
alternate_uppercase("helLLLaAlo")
# 18
def square_list(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num * num)
    return squared_numbers
square_list()
#19
i = "hello".upper()
print(i)
i = "hello".lower()
print(i)
i = "hello".capitalize()
print(i)
i = "HelLo".swapcase()
print(i)
i = "hello"
i = i.find("h")
print(i)
i = "hello"
i = len(i)
print(i)
i = ["cat", "dog", "tiger"]
position = i.index("dog")
print(position)
i = ["Hello"]
i = i.append("Hi")
print(i)
i = ["Hello"]
i = i.insert(0, "Hi")
print(i)
i = ["Hello"]
i = i.pop("Hello")
print(i)
i = ["Hello"]
i = i.remove("H")
print(i)