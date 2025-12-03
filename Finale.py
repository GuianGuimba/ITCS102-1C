import os
import json
os.system('cls')

username = input("What is your name?")

while True:
    program = input(f"Are you opening the program?\nYes or No ==>").lower().strip()
    if program == 'yes' :
        os.system('cls')
        print(f"Hi {username} Welcome to my Program!")
        while True:
            user_inputs = input("=====MENU=====\n" \
                                "A. -\n" \
                                "B. -\n" \
                                "C. -\n" \
                                "D. -\n" \
                                "==============\n\n" \
                                "=>"
                                    ).lower().strip()
            if user_inputs == 'a':
                os.system('cls')
                print("a")
                
                
                
                
                
                
                
                
                
                
                
                continue

            elif user_inputs == 'b':
                os.system('cls')
                print("b")
                continue
            elif user_inputs == 'c':
                os.system('cls')
                print("c")
                continue
            elif user_inputs == 'd':
                os.system('cls')
                print("d")
                break
            else:
                os.system('cls')
                print("Invalid Input.. Try Again")


    elif program == 'no' :
        os.system('cls')
        print("See ya!")
        break

    else:
        os.system('cls')
        print("Invalid Input..\nPlease Try again")
        continue
