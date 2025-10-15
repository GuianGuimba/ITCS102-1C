import random

name = input("Welcome Guessing Game!\nPlease Eanter your name! ==> ")

random_value = random.randint(1,6)
tries = 0
loop = True

while loop == True:
    number = eval(input("Enter a number from 1-6 => "))
    tries += 1
    if number == random_value:
        print("Yay! You won!!")
        break
    else:
        print("try again")
        continue

print(f"Hi {name} your Guess is Correct!, Number of tries is {tries}")
