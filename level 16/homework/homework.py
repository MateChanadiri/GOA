def print_num(start, end):
    x = range(start, end)
    for i in x:
        print(i)
print(print_num(int(input("Enter a start for range(): ")), int(input("Enter an end for range(): "))))

def info(name, lastname, age, academy):
    return f"Hello {name} {lastname}, Your {age} yrs old, youre a gigachad if you study at {academy}"
print(info(input("Enter name: "), input("Enter lastname: "), input("Age: "), input("academy: ")))

def Hello_User(name, lastname):
    return f"Hello, {name} {lastname}!"
print(Hello_User(input("Enter name: "), input("Enter lastname: ")))

def sum(a, b):
    sum = a + b
    return sum
print(sum(int(input("A: ")), int(input("B: "))))

def multiply(a, b, c):
    sum = a * b * c
    return sum
print(multiply(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))

foods = ["khinkali", "lobiani", "Pizza"]
def return_one_at_a_time(foods):
    for i in foods:
        print(i)
return_one_at_a_time(foods)