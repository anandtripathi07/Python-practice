# ==============================
# Basic Print and String Slicing
# ==============================
# print("hello world")
# name = "Anand"
# print(name)
# print(name[2:4])

# text = "Python is a easy and simple programming language"
# t1 = text[0:7]
# t2 = text[7:49]
# t3 = t1 + t2
# print(t3)  # Output: Python is a easy and simple programming language

# ==================
# Multiline String
# ==================
# multi_line =
# am
# Anand
# print(multi_line)

# =========================
# String Concatenation
# =========================
# n1 = "Anand tripathi"
# n2 = "Aarush kadam"
# r1 = 50
# r2 = 7
# n3 = n1 + str(r1)
# n4 = n2 + str(r2)
# print(n3)
# print(n4)

# =========================
# Input & Conditional Logic
# =========================
# name = input("What is ur name?")
# print("Name:-", name)

# x1 = input("My marks:-")
# x2 = input("Teammate marks:-")
# if(x1 > x2):
#     print("Anand have greater marks than his teammate")
# elif(x1 < x2):
#     print("Teammate has greater marks than Anand")

# ================
# List Operations
# ================
# rn = [10, 20, 30, 40, 50, 60]
# rn.append(70)
# rn.remove(10)
# del rn[1]
# print(rn)
# rn.sort()
# print(rn)
# rn.reverse()
# print(rn)
# print(rn.count(10))

# ================
# Dictionary
# ================
# y = {
#     "name": "Anand",
#     "Roll": "50"
# }
# print(y)

# ================
# Function Example
# ================
# def add():
#     num1 = input("Enter first number:")
#     num2 = input("Enter second number:")
#     sum = int(num1) + int(num2)
#     print("The sum is:", sum)
# add()

# =====================
# For Loop Examples
# =====================
# for i in range(4):
#     print(i)

# for i in range(4, 20, 2):
#     print(i)

# =====================
# Infinite While Loop
# =====================
# while True:
#     print("Your pc is hacked")

# =============================
# Guess the Number Game (3 tries)
# =============================
# import random
# RandomNumber = random.randint(1, 10)
# attempts = 3
# while attempts > 0:
#     guess = int(input("Guess the number between 1 and 10: "))
#     if guess == RandomNumber:
#         print("Congratulations! You've guessed the number.")
#         break
#     elif RandomNumber > guess:
#         print("Random Number is greater than your guess.")
#         attempts -= 1
#     elif RandomNumber < guess:
#         print("Random Number is less than your guess.")
#         attempts -= 1
#     else:
#         attempts -= 1
#         print(f"Wrong guess! You have {attempts} attempts left.")
#         if attempts == 0:
#             print(f"Sorry, the correct number was {RandomNumber}.")

instrcutions = """1.Addition
2.Substraction
3.Multiplication
4.Division
5.Continue
6.Exit"""

def addition(a,b):
    print("Addition of two numbers is:")
    return a+b

def substraction(a,b):
    print("Difference of two numbers is:")
    return a-b

def multiplication(a,b):
    print("Multiplication of two numbers is:")
    return a*b

def division(a,b):
    print("Division of two numbers is:")
    return a/b

tocontinue = True
while tocontinue == True:
    print(instrcutions)
    inst=int(input("Enter your choice: "))
    a=int(input("Enter first number."))
    b=int(input("Enter second number."))
    
    if inst == 1:
        print(addition(a,b))
    elif inst == 2:
        print(substraction(a,b))
    elif inst == 3:
        print(multiplication(a,b))
    elif inst == 4:
        print(division(a,b))
    elif inst == 5:
        tocontinue = True
    elif inst == 6:
        tocontinue = False
    else:
        print("Invalid Choice.")
