import os
import json
os.system('cls')

username = input("What is your name?").title()

while True:
    program = input(f"Are you opening the program?\nYes or No ==>").lower().strip()
    if program == 'yes' :
        os.system('cls')
        print(f"Hi! {username}, Welcome to my Program!")
        while True:
            user_inputs = input(
                                "=============== MAIN MENU ===============\n\n"
                                "A. PRINTING IN PYTHON\n"
                                "B. VARIABLES IN PYTHON\n" 
                                "C. OPERATORS IN PYTHON\n" 
                                "D. CONDITIONALS STATEMENT IN PYTHON\n"
                                "E. LOOPS IN PYTHON\n"
                                "F. LISTS IN PYTHON\n"
                                "G. FUNCTIONS IN PYTON\n"
                                "H. HELP\n"
                                "X. EXIT\n\n"
                                "=========================================\n\n"
                                "=>"
                            ).lower().strip()
            
            if user_inputs == 'a': #PRINTS
                os.system('cls')
                while True:
                    InputA = input(
                                    "===== PRINTING IN PYTHON =====\n\n"

                                    "A. DEFINITION OF print()\n"
                                    "B. EXAMPLES OF print()\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "==============================\n"
                                    "=>"
                                ).lower().strip()
                    
                    if InputA == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF print() ========\n\n"
                              
                            "The print() function prints\n"
                            "the specified message to the\n"
                            "screen, or other standard\n"
                            "output device.\n\n"
                              
                            "The message can be a string,\n"
                            "or any other object, the\n"
                            "object will be converted into\n"
                            "a string before written to\n"
                            "the screen. \n\n"

                            "You can use comma (,) in the)\n"
                            "print()to concatenate string\n"
                            "with the value of variable.\n" 
                            "using comma to cocatenate string\n" 
                            "with print() function automatically\n" 
                            "append space.\n\n"

                            "=======================================\n"
                        )
                        continue

                    elif InputA == 'b':#EXAMPLES OF PRINTS
                        os.system('cls')
                        while True:
                            ExampleInput = input(
                                                "======== EXAMPLES OF print() ========\n\n"

                                                "A. PRINTING A MESSAGE\n"
                                                "B. PRINTING MORE THAN ONE OBJECT\n"
                                                "C. PRINTING A VARIABLE\n"
                                                "D. PRINTING CONCATENATED STRING\n"
                                                "X. RETURN TO SUB MENU\n\n"

                                                "=====================================\n"
                                                "=>"
                                            ).lower().strip()
                            
                            if ExampleInput == 'a':
                                os.system('cls')
                                print(
                                    "===== PRINTING A MESSAGE =====\n\n"                              

                                    "Input:\n"
                                    "\tprint(\"Hello World\")\n"
                                    "\tprint(\"Pear\")\n"
                                    "\tprint(\"Apple\")\n\n"
                              
                                    "Output:\n"
                                    "\tHello World\n"
                                    "\tPear\n"
                                    "\tApple\n\n"
                                                           
                                    "==============================\n\n"
                                )
                                continue

                            elif ExampleInput == 'b':
                                os.system('cls')
                                print(
                                    "========== PRINTING MORE THAN ONE OBJECT ==========\n\n"

                                    "Input:\n"
                                    "\tprint(\"Hello World\", \"Pear\", \"Apple\")\n"
                                    f"\tprint(\"Hi\", \"{username}\")\n"
                                    "\tprint(\"One\", \"Two\", \"Three\")\n\n"

                                    "Output:\n"
                                    "\tHello World Pear Apple\n"
                                    f"\tHi {username}\n"
                                    "\tOne Two Three\n\n"

                                    "===================================================\n\n"                                                                   
                                )
                                continue

                            elif ExampleInput == 'c':
                                os.system('cls')
                                print(
                                    "===== PRINTING A VARIABLE =====\n\n"

                                    "Input:\n\n"
                                    "\tx = \"Hello World\"\n"
                                    "\tprint(x)\n\n"
                                    f"\tname = \"{username}\"\n"
                                    "\tprint(name)\n\n"

                                    "Output:\n"
                                    "\tHello World\n"
                                    f"\t{username}\n\n"
                                    "===============================\n"
                                )
                                continue

                            elif ExampleInput == 'd':
                                os.system('cls')
                                print(
                                    "===== PRINTING CONCATENATED STRING =====\n\n"

                                    "Input:\n\n"
                                    "\tstring1= \"Hello \"\n"
                                    f"\tstring2 = \"{username} \"\n"
                                    "\tstring3 = \"I'm a \"\n"
                                    "\tstring4 = \"Student \"\n"
                                    "\tprint(string1+string2+string3+string4)\n\n"                                                                       

                                    "Output:\n"
                                    f"\tHello {username} I'm a Student\n\n"
                                
                                    "========================================\n"
                                )
                                continue

                            elif ExampleInput == 'x':
                                os.system('cls')
                                print("Returning to SUB MENU!")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Input.. Please Try Again..")
                                continue                                                                                                 
                        continue

                    elif InputA == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break
                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                    
            elif user_inputs == 'b': #VARIABLES
                os.system('cls')
                while True:
                    InputB = input(
                                    "===== VARIABLES IN PYTHON =====\n\n"

                                    "A. DEFINITION OF VARIABLE\n"
                                    "B. EXAMPLES OF VARIABLES\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "==============================\n"
                                    "=>"
                                ).lower().strip()
                    if InputB == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF VARIABLE ========\n\n"

                            "In Python, a variable is a named storage\n"
                            "location that holds a value. It acts as\n"
                            "a symbolic name or identifier that refers\n"
                            "to an object or data in the computer's\n"
                            "memory.\n\n"
                            
                            "========================================\n"
                        )
                        continue

                    if InputB == 'b':
                        os.system('cls')
                        print(
                            "===== EXAMPLE OF VARIABLES =====\n\n" \
                            
                            "Input:\n" \
                            "\tString = \"Hello World\"\n"                           
                            "\tintegers = 21 + 48\n"
                            "\tevaluation = input(\"Input your grades here\") #user inputs 95\n\n"

                            "\tprint(string)\n"
                            "\tprint(integers)\n"
                            "\tprint(evaluation)\n\n"

                            "Output:\n"
                            "\tHello World\n"
                            "\t69\n"
                            "\t95\n\n"
                        )


                    elif InputB == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue

                continue
            
            elif user_inputs == 'c': #OPERATORS
                os.system('cls')
                while True:
                    InputC = input(
                                    "===== OPERATORS IN PYTHON =====\n\n"

                                    "A. DEFINITION OF OPERATOR\n"
                                    "B. EXAMPLES OF OPERATOR\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "==============================\n"
                                    "=>"
                                ).lower().strip()
                    if InputC == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF OPERATOR ========\n\n"

                            "In Python, operators are special symbols\n"
                            "or keywords that perform operations on\n"
                            "variables and values, known as operands.\n\n"

                            "========================================\n"
                        )
                        continue

                    elif InputC == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue

            elif user_inputs == 'd': #CONDITIONAL
                os.system('cls')
                while True:
                    InputD = input(
                                    "== CONDITIONALS STATEMENT IN PYTHON ==\n\n"

                                    "A. DEFINITION OF CONDITIONAL STATEMENT\n"
                                    "B. EXAMPLES OF CONDITIONAL STATEMENT\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "======================================\n"
                                    "=>"
                                ).lower().strip()
                    if InputD == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF CONDITIONAL STATEMENT ========\n\n"
                                                   
                            "Conditional statements in Python are used\n"
                            "to execute certain blocks of code based\n"
                            "on specific conditions. These statements\n"
                            "help control the flow of a program, making\n"
                            "it behave differently in different\n"
                            "situations.\n\n"

                            "======================================================\n"
                        )
                        continue

                    elif InputD == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue
            
            elif user_inputs == 'e': #LOOPS
                os.system('cls')
                while True:
                    InputE = input(
                                    "===== LOOPS IN PYTHON =====\n\n"

                                    "A. DEFINITION OF LOOPS\n"
                                    "B. EXAMPLES OF LOOPS\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "===========================\n"
                                    "=>"
                                ).lower().strip()
                    if InputE == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF LOOPS ========\n\n"

                            "In Python, loops are control flow\n"
                            "statements that enable the repeated\n"
                            "execution of a block of code.\n\n"

                            "=====================================\n"
                        )
                        continue

                    elif InputE == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue
            
            elif user_inputs == 'f': #LIST
                os.system('cls')
                while True:
                    InputF = input(
                                    "===== LISTS IN PYTHON =====\n\n"

                                    "A. DEFINITION OF LISTS\n"
                                    "B. EXAMPLES OF LISTS\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "===========================\n"
                                    "=>"
                                ).lower().strip()
                    if InputF == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF LISTS ========\n\n"

                            "In Python, a list is a built-in data\n"
                            "type used to store an ordered,\n"
                            "mutable collection of items. These\n"
                            "items can be of various data types,\n"
                            "including numbers, strings, booleans,\n"
                            "other lists, or even more complex\n"
                            "objects.\n\n"

                            "=====================================\n"
                        )
                        continue

                    elif InputF == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue
            
            elif user_inputs == 'g': #FUNCTION
                os.system('cls')
                while True:
                    InputG = input(
                                    "===== FUNCTION IN PYTHON =====\n\n"

                                    "A. DEFINITION OF FUNCTION\n"
                                    "B. EXAMPLES OF FUNCTION\n"                                                                   
                                    "X. RETURN TO MAIN MENU\n\n"

                                    "===========================\n"
                                    "=>"
                                ).lower().strip()
                    if InputG == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF FUNCTION ========\n\n"

                            "In Python, a function is a named,\n"
                            "reusable block of code designed to\n"
                            "perform a specific task. Functions are\n"
                            "fundamental to structured programming,\n"
                            "promoting code modularity, reusability,\n"
                            "and readability.\n\n"

                            "========================================\n"
                        )
                        continue

                    elif InputG == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue

            elif user_inputs == 'x': #EXIT
                os.system('cls')
                print("x")
                break
            
            else:#Invalid 1
                os.system('cls')
                print("Invalid Input.. Please Try Again")

    elif program == 'no' :
        os.system('cls')
        print("See ya!")
        break

    else:
        os.system('cls')
        print("Invalid Input..\nPlease Try again")
        continue
