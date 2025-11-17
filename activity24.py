from activity23_1 import *

print("WELCOME TO MY COMPUTER PROGRAM")
name = input("Hi Visitor!, What is your name?\n")
print(f"Hi {name}, select from the option below\nA - Greet Name\nB- Greet with name, age, location\nC-Triangle\nD- Factorial\nE- Exit")

Loop = True
while Loop == True:
    Input = input("\nChoose for A - E => ").lower()
    if Input == 'a':
        name = input("Please state your name")
        another(name)
        continue

    elif Input == 'b':
        name = input("Please state your name => ")
        location = input("Please state your location =>")
        age = input("Please state your age => ")
        NLA(name,location,age)
        continue

    elif Input == 'c':
        count = eval(input("in a scale of 1-10 how large you want your triangle be?"))
        if count < 11:
            Triangle(count)
        elif count == 67:
            print("Please Stop")
        else:
            print("Too large man")
        continue

    elif Input == 'd':
        number = eval(input("Input any number => "))
        print(f"Factorial of {number} is {Factorial(number)} ")
        continue

    elif Input == 'e':
        print("You exited the program")
        break
    
    else:
        print("Invalid Input.. Try Again")
        continue
