


def Hello_world():
    return "Hello World!"
print(Hello_world())

def Hello_name(name):
    return f"Hello, {name}!"
print(Hello_name(input("Enter name: ")))

def multiply(a, b):
    return a * b
print(multiply(int(input("Enter a: ")), int(input("Enter b: "))))

def adult_or_not():
    age = int(input("Enter age: "))
    if age <= 17:
        return "Not adult"
    else:
        return "Adult"
print(adult_or_not())

def sum():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    return a + b + c
print(sum())

def pass_or_no():
    score = int(input("Your score (0-100): "))
    if score >= 80:
        return "Pass"
    else:
        return "Didnt pass"
print(pass_or_no())


