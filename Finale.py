import os
import sys
import json
import random
import io
import contextlib

os.system('cls')

def codingactivity(task,expected_output,expected_input):
    os.system('cls')
    print(
        "==================== CODE ACTIVITY ====================\n\n"

        f"Task: \n\t{task}\n\n"
        f"Expected Output: {expected_output}\n"
        f"Expected Input: {expected_input}\n\n"
        "Type your code below.\n"
        "Type END on a new line when you're done:\n"
        )
    
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)

    user_code = "\n".join(code_lines)

    f = io.StringIO()

    try:
        with contextlib.redirect_stdout(f):
            exec(user_code)
        output = f.getvalue().strip()
    except Exception as e:
        print(
            "Your code has an Error\n"
            f"Error: {e}")
        input(
            "\n=======================================================\n\n"
            "Press ENTER to return...")
        return
        
    if output in expected_output.strip() and expected_input in user_code:
        print(
            "\nCorrect! the output and input matches the expected result!\n"
            "\n=======================================================\n"
        )
        input("Press Enter to return...")
        os.system('cls')

    else:
        print(
            "\nIncorrect output or Missing input. Try again!"
            f"\nYour output: {output}"
            f"\nExpected Output: {expected_output}"
            f"\nExpected Input: {expected_input}"
        )
        input(
            "\n=======================================================\n"
            "Press Enter to return...")
        os.system('cls')

username = input("What is your name? ").title()

while True:
    program = input(f"Are you opening the program?\nYes or No ==> ").lower().strip()
    if program == 'yes' :
        os.system('cls')
        print(f"Hi! {username}, Welcome to my Program!")
        while True:
            user_inputs = input(
                                "=============== MAIN MENU ===============\n\n"
                                
                                "[A] PRINTING IN PYTHON\n"
                                "[B] VARIABLES IN PYTHON\n" 
                                "[C] OPERATORS IN PYTHON\n" 
                                "[D] CONDITIONALS STATEMENT IN PYTHON\n"
                                "[E] LOOPS IN PYTHON\n"
                                "[F] LISTS IN PYTHON\n"
                                "[G] DICTIONARY IN PYTHON\n"
                                "[H] FUNCTIONS IN PYTON\n"
                                "[X] EXIT\n\n"

                                "=========================================\n\n"
                            ).lower().strip()
            
            if user_inputs == 'a': #PRINTS
                os.system('cls')
                while True:
                    InputA = input(
                                    "===== PRINTING IN PYTHON =====\n\n"

                                    "[A] DEFINITION OF print()\n"
                                    "[B] EXAMPLES OF print()\n"
                                    "[C] ACTIVITY\n"                                                                   
                                    "[X] RETURN TO MAIN MENU\n\n"

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
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputA == 'b':#EXAMPLES OF PRINTS
                        os.system('cls')
                        while True:
                            ExampleInput = input(
                                                "======== EXAMPLES OF print() ========\n\n"

                                                "[A] PRINTING A MESSAGE\n"
                                                "[B] PRINTING MORE THAN ONE OBJECT\n"
                                                "[C] PRINTING A VARIABLE\n"
                                                "[D] PRINTING CONCATENATED STRING\n"
                                                "[X] RETURN TO SUB MENU\n\n"

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
                                input("Press ENTER to return to the menu...")
                                os.system('cls')
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
                                input("Press ENTER to return to the menu...")
                                os.system('cls')
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
                                input("Press ENTER to return to the menu...")
                                os.system('cls')
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
                                input("Press ENTER to return to the menu...")
                                os.system('cls')
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

                    elif InputA == 'c':
                        codingactivity(
                            "For this activity we will use print() function\n"
                            "and the Expected Output must be \"Hello World\"",

                            "Hello World",

                            "print("
                            )  
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

                                    "[A] DEFINITION OF VARIABLE\n"
                                    "[B] EXAMPLES OF VARIABLES\n"
                                    "[C] ACTIVITY\n"                                                                     
                                    "[X] RETURN TO MAIN MENU\n\n"

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
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputB == 'b':
                        os.system('cls')
                        print(
                            "========================= EXAMPLE OF VARIABLES =========================\n\n"
                            
                            "Input:\n" 
                            "\tString = \"Hello World\"\n"                           
                            "\tintegers = 21 + 51\n"
                            "\tevaluation = input(\"Input your grades here\") #user inputs 95\n\n"

                            "\tprint(string)\n"
                            "\tprint(integers)\n"
                            "\tprint(evaluation)\n\n"

                            "Output:\n"
                            "\tHello World\n"
                            "\t72\n"
                            "\t95\n\n"

                            "========================================================================\n\n"
                        )
                        input("Press ENTER to return to the menu...")
                        os.system('cls')

                    elif InputB == 'c':
                        codingactivity(
                            "For this activity we will use VARIABLES.\n"
                            "This activity must have two Variables,\n"
                            "a and b. Specifically assign each one\n"
                            "of them with their respected 'WORD'.\n"
                            "use concatenation in print().\n"
                            "expected output should be 'Hello World'",

                            "HelloWorld",

                            "="
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

                                    "[A] DEFINITION OF OPERATOR\n"
                                    "[B] EXAMPLES OF OPERATOR\n"
                                    "[C] ACTIVITY\n"                                                                  
                                    "[X] RETURN TO MAIN MENU\n\n"

                                    "==============================\n"
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
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue
                    elif InputC == 'b': #EXAMPLES OF OPERATORS
                        os.system('cls')
                        while True:
                            OperatorsInput = input(
                                "===== EXAMPLE OF OPERATORS =====\n\n"

                                "[A] ARITHMETIC OPERATOR\n"
                                "[B] ASSIGNMENT OPERATOR\n"
                                "[C] RELATIONAL OPERATOR\n"
                                "[D] LOGICAL OPERATOR\n"
                                "[X] RETURN TO SUB MENU\n\n"

                                "================================\n"
                            ).lower().strip()
                            if OperatorsInput == 'a': #ARITHMETIC OPERATOR
                                os.system('cls')
                                while True:
                                    AriChoice = input(
                                        "===== ARITHMETIC OPERATOR =====\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "===============================\n"
                                    ).lower().strip()

                                    if AriChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "===== DEFINITION OF ARITHMETIC OPERATOR =====\n\n"

                                            "Arithmetic operators are symbols used in\n"
                                            "Python to perform basic mathematical\n"
                                            "operations on numbers or variables.\n\n"

                                            "=============================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')

                                    elif AriChoice == 'b':
                                        os.system('cls')
                                        print("===== EXAMPLE OF ARITHMETIC OPERATOR =====\n")

                                        while True:
                                            try:
                                                a = float(input("Input 1st number => "))
                                                b = float(input("Input 2nd number => "))
                                                break
                                            except ValueError:
                                                os.system('cls')
                                                print("\nInvalid Input! Please enter a number only!\n")

                                        Addition = a + b
                                        Subtracton = a - b
                                        Multiplication = a * b
                                        Division = a / b
                                        Floor_Division = a // b
                                        Modulus = a % b
                                        Exponent = a ** b

                                        print("\n"
                                        f"Addition = {Addition}\n"
                                        f"Subtraction = {Subtracton}\n"
                                        f"Multiplication = {Multiplication}\n"
                                        f"Division = {Division}\n"
                                        f"Floor Division (Whole Number) = {Floor_Division}\n"
                                        f"Modulus (Remainder) = {Modulus}\n"
                                        f"Exponent (Power) = {Exponent}\n\n"
                                        )

                                        ExAriChoice = input(
                                            "============================================\n\n"
                                            "Do you want to see inside of the code? (Yes/No) ").lower().strip()

                                        if ExAriChoice == 'yes':
                                            os.system('cls')
                                            print(
                                            "=================================================================\n\n"
                                            "while True\n"
                                            "\tTry:\n"
                                            "\t\ta = eval(input(\"Input 1st number => \"))\n"
                                            "\t\tb = eval(input(\"Input 2nd number => \"))\n"
                                            "\t\tbreak\n"
                                            "\texcept ValueError:\n"
                                            "\t\tos.system('cls')\n"
                                            "\t\tprint(\"\\nInvalid Input! Please enter a number only!\\n)\n\n"

                                            "Addition = a + b\n"
                                            "Subtracton = a - b\n"
                                            "Multiplication = a * b\n"
                                            "Division = a / b\n"
                                            "Floor_Division = a // b\n"
                                            "Modulus = a % b\n"
                                            "Exponent = a ** b\n\n"

                                            "print(\"\\n\"\n"
                                            "f\"Addition = \{Addition}\\n\"\n"
                                            "f\"Subtraction = {Subtracton}\\n\"\n"
                                            "f\"Multiplication = {Multiplication}\\n\"\n"
                                            "f\"Division = {Division}\n"
                                            "f\"Floor Division (Whole Number) = {Floor_Division}\\n\"\n"
                                            "f\"Modulus (Remainder) = {Modulus}\\n\"\n"
                                            "f\"Exponent (Power) = {Exponent}\\n\\n\n"
                                            ")\n\n"
                                            "=================================================================\n\n"
                                            )
                                            input("Press ENTER to return to the menu...")
                                            os.system('cls')
                                        
                                        else:
                                            os.system('cls')
                                            print("Returning...")

                                    elif AriChoice == 'x':
                                        os.system('cls')
                                        print("Returning...")
                                        break
                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue

                            elif OperatorsInput == 'b': #ASSIGNMENT OPERATOR
                                os.system('cls')
                                while True:
                                    AssiChoice = input(
                                        "===== ASSIGNMENT OPERATOR =====\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "===============================\n"
                                    ).lower().strip()

                                    if AssiChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "===== DEFINITION OF ASSIGNMENT OPERATOR =====\n\n"                                       

                                            "it's one or two symbols that are used to\n"
                                            "assign a value to a variable.\n\n"

                                            "=============================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                    
                                    elif AssiChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "===== EXAMPLE OF ASSIGNMENT OPERATOR =====\n\n"

                                            "Input:\n"
                                            "\tx += 10\n"
                                            "\tx += 10\n" 
                                            "\tx -= 5\n\n"

                                            "Output:\n"
                                            "\t15\n\n"

                                            "==========================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                    
                                    elif AssiChoice == 'x':
                                        os.system('cls')
                                        print("Returning...")
                                        break
                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue

                            elif OperatorsInput == 'c': #RELATIONAL OPERATOR
                                os.system('cls')
                                while True:
                                    RelaChoice = input(
                                        "===== RELATIONAL OPERATOR =====\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "================================\n"
                                    ).lower().strip()

                                    if RelaChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "===== DEFINITION OF RELATIONAL OPERATOR =====\n\n"                                       

                                            "This are used to compare two values and\n"
                                            "determine their relationship.\n"
                                            "(also called comparison operators)\n\n"

                                            "=============================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                    elif RelaChoice == 'b':
                                        os.system('cls')
                                        print("========== EXAMPLE OF RELATIONAL OPERATOR =========\n\n")
                                        
                                        while True:
                                            try:
                                                a = float(input("Input 1st number => "))
                                                b = float(input("Input 2nd number => "))
                                                break
                                            except ValueError:
                                                os.system('cls')
                                                print("\nInvalid Input! Please enter a number only!\n")

                                        Equal_to = a == b
                                        Not_Equal_to = a != b
                                        Greater_than = a > b
                                        Less_than = a < b
                                        Greater_than_or_Equal_to = a >= b
                                        Less_than_or_Equal_to = a <= b

                                        print("\n"
                                        f"{a} Equal to {b} = {Equal_to}\n"
                                        f"{a} Not Equal to {b} = {Not_Equal_to}\n"
                                        f"{a} Greater than {b} = {Greater_than}\n"
                                        f"{a} Less than {b} = {Less_than}\n"
                                        f"{a} Greater than or Equal to {b} = {Greater_than_or_Equal_to}\n"
                                        f"{a} Less Than or Equal to {b} = {Less_than_or_Equal_to}\n\n"
                                        )

                                        ExRelaChoice = input(
                                            "======================================================\n\n"
                                            "Do you want to see inside of the code? (Yes/No) ").lower().strip()
                                        if ExRelaChoice == 'yes':
                                            os.system('cls')
                                            print(
                                            "=================================================================\n\n"
                                            "while True\n"
                                            "\tTry:\n"
                                            "\t\ta = eval(input(\"Input 1st number => \"))\n"
                                            "\t\tb = eval(input(\"Input 2nd number => \"))\n"
                                            "\t\tbreak\n"
                                            "\texcept ValueError:\n"
                                            "\t\tos.system('cls')\n"
                                            "\t\tprint(\"\\nInvalid Input! Please enter a number only!\\n)\n\n"

                                            "Equal_to = \t\t\ta == b\n"
                                            "Not_Equal_to = \t\t\ta != b\n"
                                            "Greater_than = \t\t\ta > b\n"
                                            "Less_than = \t\t\ta < b\n"
                                            "Greater_than_or_Equal_to = \ta >= b\n"
                                            "Less_than_or_Equal_to = \ta <= b\n"

                                            "print(\"\\n\"\n"
                                            "f\"{a} Equal to {b} = {Equal_to}\\n\n"
                                            "f\"{a} Not Equal to {b} = {Not_Equal_to}\\n\n"
                                            "f\"{a} Greater than {b} = {Greater_than}\\n\n"
                                            "f\"{a} Less than {b} = {Less_than}\\n\n"
                                            "f\"{a} Greater than or Equal to {b} = {Greater_than_or_Equal_to}\\n\n"
                                            "f\"{a} Less Than or Equal to {b} = {Less_than_or_Equal_to}\\n\\n\n"
                                            ")\n\n"
                                            "=================================================================\n\n"
                                            )
                                            input("Press ENTER to return to the menu...")
                                            os.system('cls')
                                        else:
                                            os.system('cls')
                                            print("Returning...")

                                    elif RelaChoice == 'x':
                                        os.system('cls')
                                        print("Returning...")
                                        break
                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue      

                            elif OperatorsInput == 'd': #LOGICAL OPERATOR
                                os.system('cls')
                                while True:
                                    LogiChoice = input(
                                        "===== LOGICAL OPERATOR =====\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "============================\n"
                                    ).lower().strip()
                                    if LogiChoice == ('a'):
                                        os.system('cls')
                                        print(
                                            "===== DEFINITION OF LOGICAL OPERATOR =====\n\n"                                       

                                            "This are used to combine multiple\n"
                                            "conditions or to invert a condition.\n"
                                            "They return True or False based on the\n"
                                            "logic applied.\n\n"

                                            "==========================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')

                                    elif LogiChoice == ('b'):
                                        os.system('cls')
                                        print(
                                            "========== EXAMPLE OF RELATIONAL OPERATOR ==========\n\n" 

                                            "Operator:\n"
                                            "\tand\n"
                                            "\tor\n"
                                            "\tnot\n\n"

                                            "Meaning:\n"
                                            "\tTrue if both conditions are true\n"
                                            "\tTrue if at least one condition is true\n"
                                            "\tReverses the result (True → False, False → True)\n\n"

                                            "Input:\n"
                                            "\ta = (5 > 2) and (3 < 4)\n"
                                            "\tb = (7 < 2) and (4 > 2)\n\n"

                                            "\tc = (5 > 2) or (3 > 10)\n"
                                            "\td = (5 < 2) or (11 < 9)\n\n"

                                            "\te = not (3 > 4)\n"
                                            "\tf = not (4 > 2)\n\n"

                                            "print(\n"
                                            "f\"{a}\\n\"\n"
                                            "f\"{b}\\n\"\n"
                                            "f\"{c}\\n\"\n"
                                            "f\"{d}\\n\"\n"
                                            "f\"{e}\\n\"\n"
                                            "f\"{f}\\n\"\n"
                                            ")\n\n"

                                            "Output:\n"
                                            "\tTrue\n"
                                            "\tFalse\n"
                                            "\tTrue\n"
                                            "\tFalse\n"
                                            "\tTrue\n"
                                            "\tFalse\n\n"                                        

                                            "====================================================\n\n" 
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                    
                                    elif LogiChoice == 'x':
                                        os.system('cls')
                                        print("Returning...")
                                        break
                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue      

                            elif OperatorsInput == 'x':
                                os.system('cls')
                                print("Returning to SUB MENU!")
                                break
                            else:
                                os.system('cls')
                                print("Invalid Input.. Please Try Again..")
                                continue
                    
                    elif InputC == 'c':
                        codingactivity(
                            "For this activity we will use OPERATORS.\n"
                            "This activity must have operator and output\n"
                            "of 8",

                            "8",

                            "+="
                            )
                        
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

                                    "[A] DEFINITION OF CONDITIONAL STATEMENT\n"
                                    "[B] EXAMPLE OF CONDITIONAL STATEMENT\n"
                                    "[C] ACTIVITY\n"                                                                   
                                    "[X] RETURN TO MAIN MENU\n\n"

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
                        input("Press ENTER to return to the menu...")
                        os.system('cls')

                        continue

                    if InputD == 'b': #EXAMPLE CONDITIONAL STATEMENT
                        os.system('cls')
                        print("===== EXAMPLE OF CONDITIONAL STATEMENT =====\n\n")
                        while True:
                            try:
                                temp = float(input("Input the temperature here (In Celsius) \n==> "))
                                break
                            except ValueError:
                                os.system('cls')
                                print("\nInvalid Input! Please enter a number only!\n")

                        if temp <= 0:
                            print("Freezing Temperature")
                        elif temp >= 1 and temp <= 20:
                            print("Extremely Cold")
                        elif temp >= 21 and temp <= 30:
                            print("Moderately Cold")
                        elif temp >= 31 and temp <= 37:
                            print("Lukewarm")
                        elif temp >= 38 and temp <= 45:
                            print("Hot")
                        elif temp >= 46 and temp <= 50:
                            print("Boiling Hot")
                        elif temp >= 51:
                            print("Dangerously Hot!")
                        else :
                            print("Too low or Too Hot")

                        ExCondiChoice = input(
                                            "\n============================================\n\n"
                                            "Do you want to see inside of the code? (Yes/No) ").lower().strip()
                        if ExCondiChoice == 'yes':
                                            os.system('cls')
                                            print(
                                            "=================================================================\n\n"

                                            "while True:\n"
                                            "\ttry:\n"
                                                "\t\ttemp = float(input(\"Input the temperature here (In Celsius) \\n==> \"))\n"
                                                "\t\tbreak\n"
                                            "\texcept ValueError:\n"
                                                "\t\tos.system('cls')\n"
                                                "\t\tprint(\"\\nInvalid Input! Please enter a number only!\\n\")\n\n"

                                            "if temp <= 0:\n"
                                                "\tprint(\"Freezing Temperature\")\n"
                                            "elif temp >= 1 and temp <= 20:\n"
                                                "\tprint(\"Extremely Cold\")\n"
                                            "elif temp >= 21 and temp <= 30:\n"
                                                "\tprint(\"Moderately Cold\")\n"
                                            "elif temp >= 31 and temp <= 37:\n"
                                                "\tprint(\"Lukewarm\")\n"
                                            "elif temp >= 38 and temp <= 45:\n"
                                                "\tprint(\"Hot\")\n"
                                            "elif temp >= 46 and temp <= 50:\n"
                                                "\tprint(\"Boiling Hot\")\n"
                                            "elif temp >= 51:\n"
                                                "\tprint(\"Dangerously Hot!\")\n"
                                            "else :\n"
                                                "\tprint(\"Too low or Too Hot\")\n\n"

                                            "=================================================================\n\n"
                                            )
                                            input("Press ENTER to return to the menu...")
                                            os.system('cls')

                        else:
                            os.system('cls')
                            print("Returning...")

                    elif InputD == 'c':
                        codingactivity(
                            "For this activity we will use the\n"
                            "condtional statement. This activity\n"
                            "must have 'if' and 'else' and\n"
                            "if variable x is yes (x = yes), then the\n"
                            "output must be TRUE",

                            "TRUE",

                            "if"
                        )
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

                                    "[A] DEFINITION OF LOOPS\n"
                                    "[B] EXAMPLES OF LOOPS\n"
                                    "[C] ACTIVITY\n"                                                                   
                                    "[X] RETURN TO MAIN MENU\n\n"

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
                        input("Press ENTER to return to the menu...")
                        os.system('cls')

                        continue
                    elif InputE == 'b':
                        os.system('cls')
                        while True:
                            Loopchoice = input(
                                "===== EXAMPLES OF LOOPS =====\n\n"
                                
                                "[A] FOR LOOP\n"
                                "[B] WHILE LOOP\n"
                                "[X] RETURN TO SUB MENU\n\n"

                                "=============================\n\n"
                                )
                            
                            if Loopchoice == 'a': #FOR LOOP
                                os.system('cls')
                                while True:
                                    ForChoice = input(
                                        "=========== FOR LOOPS ===========\n\n"
                                        
                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "=================================\n\n"
                                    ).lower().strip()
                                    if ForChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "===== FOR LOOP DEFINITION =====\n\n"
                                            
                                            "It' a command used to repeat a\n"
                                            "set of instructions for each\n"
                                            "item in a list, range, or\n"
                                            "sequence.\n\n"

                                            "===============================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')

                                    elif ForChoice == 'b':
                                        os.system('cls')
                                        print("==================== EXAMPLE OF FOR LOOP ====================\n")
                                        while True:
                                            try:
                                                number = int(input("Input a number from 1-5 =>"))
                                                if 1 <= number <= 5:
                                                    break
                                                else:
                                                    raise ValueError
                                                
                                            except ValueError:
                                                os.system('cls')
                                                print("\nInvalid Input! Please enter an Integer range from 1-5 only!\n")
                                        print("\n Example 1:\n")

                                        for x in range (number):
                                            print("Hello World")
                                        print("\n Example 2:\n")

                                        for i in range (1,number,1):
                                            for x in range(1,i+1,1):
                                                print("*",end=" ")
                                            print( )
                                        print("\n Example 3:\n")

                                        for i in range(1,number,1):
                                            for x in range(number,i,-1):
                                                print(" ",end=" ")
                                            for y in range(1,i,1):
                                                print("*",end=" ")
                                            for z in range(1,i+ 1):
                                                print("*",end=" ")
                                            print( )
                                        
                                        ExForChoice = input(
                                            "=============================================================\n\n"
                                            "Do you want to see inside of the code? (Yes/No) ").lower().strip()

                                        if ExForChoice == 'yes': #For Loop Example > String
                                            os.system('cls')
                                            print(
                                            "=================================================================================================\n\n"

                                            "while True:\n"
                                                "\ttry:\n"
                                                    "\t\tnumber = int(input(\"Input a number from 1-5 =>\"))\n"
                                                    "\t\tif 1 <= number <= 5:\n"
                                                        "\t\t\tbreak\n"
                                                    "\t\telse:\n"
                                                        "\t\t\traise ValueError\n\n"
                                                    
                                                    "\t\texcept ValueError:\n"
                                                        "\t\t\tos.system('cls')\n"
                                                        "\t\t\tprint(\"\\nInvalid Input! Please enter an Integer range from 1-5 only!\\n\")\n\n"

                                            "Example 1:\n\n"                                               

                                                "\tfor x in range (number):\n"
                                                    "\t\tprint(\"Hello World\")\n"

                                            "Example 2:\n\n"                                                

                                                "\tfor i in range (1,number,1):\n"
                                                    "\t\tfor x in range(i,number+1):\n"
                                                        "\t\t\tprint(\"*\",end=\" \")\n"
                                                    "\t\tprint( )\n\n"

                                            "Example 3:\n\n" 

                                                "\tfor i in range(1,number,1):\n"
                                                    "\t\tfor x in range(number,i,-1):\n"
                                                        "\t\t\tprint(\" \",end=\" \")\n"
                                                    "\t\tfor y in range(1,i,1):\n"
                                                        "\t\t\tprint(\"*\",end=\" \")\n"
                                                    "\t\tfor z in range(1,i+ 1):\n"
                                                        "\t\t\tprint(\"*\",end=" ")\n"
                                                    "\tprint( )\n\n"

                                            "=================================================================================================\n\n"
                                            )
                                       
                                            input("Press ENTER to return to the menu...")
                                            os.system('cls')

                                        else:
                                            os.system('cls')
                                            print("Returning...")


                                    elif ForChoice == 'x':
                                        os.system('cls')
                                        print("Returning!")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue

                            elif Loopchoice == 'b': #WHILE LOOP
                                os.system('cls')
                                while True:
                                    WhiChoice = input(
                                        "=========== WHILE LOOP ===========\n\n"
                                        
                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "===================================\n\n"
                                    ).lower().strip()

                                    if WhiChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "===== WHILE LOOP DEFINITION =====\n\n"
                                            
                                            "It's a control structure that\n"
                                            "repeats a block of code as long\n"
                                            "as a condition is true.\n\n"

                                            "=================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')

                                    elif WhiChoice == 'b': #Example of While Loop > Code
                                        os.system('cls')
                                        print("==================== EXAMPLE OF WHILE LOOP ====================\n")
                                        while True:
                                            try:
                                                number = int(input("Input a number from 1-5 =>"))
                                                if 1 <= number <= 5:
                                                    break
                                                else:
                                                    raise ValueError
                                                
                                            except ValueError:
                                                os.system('cls')
                                                print("\nInvalid Input! Please enter an Integer range from 1-5 only!\n")
                                        print("\nExample 1:\n")

                                        x = 1
                                        while x <= number:
                                            print(x)
                                            x += 1

                                        print("\nExample 2:\n")

                                        isDirty = True
                                        while isDirty == True:
                                            wash_again = input("Continue washing the clothes? (yes or no) ").lower()

                                            if wash_again == "yes":
                                                print("Washing the clothes again . . . ")
                                                continue
                                            else:
                                                print("Washing stops now . . .")
                                                break

                                        print("\nExample 3:\n")

                                        #import random

                                        print("Welcome to Guessing Game!")

                                        random_value = random.randint(1,number)
                                        tries = 0
                                        loop = True

                                        while loop == True:
                                            try:
                                                number = int(input(f"Enter a number from 1-{number} => "))
                                                tries += 1
                                                if number == random_value:
                                                    print("Yay! You won!!")
                                                    break
                                                else:
                                                    print("try again")
                                                    continue
                                            except ValueError:
                                                print("\nInvalid Input! Please enter an Integer range from 1-5 only!\n")

                                        print(f"Hi {username} your Guess is Correct!, Number of tries is {tries}")

                                        ExWhichoice = input(
                                            "===============================================================\n"                                            
                                            "Do you want to see inside of the code? (Yes/No) "
                                            ).lower().strip()

                                        if ExWhichoice == 'yes': #Example While Loop > String
                                            os.system('cls')
                                            print(
                                            "=================================================================================================\n\n"

                                            "while True:\n"
                                                "\ttry:\n"
                                                    "\t\tnumber = int(input(\"Input a number from 1-5 =>\"))\n"
                                                    "\t\tif 1 <= number <= 5:\n"
                                                        "\t\t\tbreak\n"
                                                    "\t\telse:\n"
                                                        "\t\t\traise ValueError\n\n"
                                                    
                                                    "\t\texcept ValueError:\n"
                                                        "\t\t\tos.system('cls')\n"
                                                        "\t\t\tprint(\"\\nInvalid Input! Please enter an Integer range from 1-5 only!\\n\")\n\n"

                                            "Example 1:\n\n"

                                            "x = 1\n"
                                            "while x <= number:\n"
                                                "\tprint(x)\n"
                                                "\tx += 1\n\n"

                                            "Example 2:\n\n" 

                                            "isDirty = True\n"
                                            "while isDirty == True:\n"
                                                "\twash_again = input(\"Continue washing the clothes? (yes or no) \").lower()\n\n"

                                                "\tif wash_again == \"yes\":\n"
                                                    "\t\tprint(\"Washing the clothes again . . . \")\n"
                                                    "\t\tcontinue\n"
                                                "\telse:\n"
                                                    "\t\tprint(\"Washing stops now . . .\")\n"
                                                    "\t\tbreak\n\n"

                                            "Example 3:\n\n"
                                            
                                            "import random\n\n"

                                            "print(\"Welcome to Guessing Game!\")\n\n"

                                            "random_value = random.randint(1,number)\n"
                                            "tries = 0\n"
                                            "loop = True\n\n"

                                            "while loop == True:\n"
                                                "\tnumber = eval(input(f\"Enter a number from 1-{number} => \"))\n"
                                                "\ttries += 1\n"
                                                "\tif number == random_value:\n"
                                                    "\t\tprint(\"Yay! You won!!\")\n"
                                                    "\t\tbreak\n"
                                                "\telse:\n"
                                                    "\t\tprint(\"try again\")\n"
                                                    "\t\tcontinue\n\n"

                                            "print(f\"Hi {username} your Guess is Correct!, Number of tries is {tries}\")\n\n"

                                            "=================================================================================================\n\n"
                                            )
                                            input("Press ENTER to return to the menu...")
                                            os.system('cls')

                                        else:
                                            os.system('cls')
                                            print("Returning...")
                                    
                                    elif WhiChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue

                            elif Loopchoice == 'x':
                                os.system('cls')
                                print("Returning to SUB MENU!")
                                break

                            else:
                                os.system('cls')
                                print("Invalid Input.. Please Try Again..")
                                continue
                    
                    elif InputE == 'c':
                        codingactivity(
                            "For this activity we will use loop.\n"
                            "This activity must use for loop to print\n"
                            "5 Hello Worlds",

                            "Hello World\n"
                            "Hello World\n"
                            "Hello World\n"
                            "Hello World\n"
                            "Hello World\n",

                            "for"
                        )
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

                                    "[A] DEFINITION OF LISTS\n"
                                    "[B] EXAMPLES OF LISTS\n"
                                    "[C] ACTIVITY\n"                                                                  
                                    "[X] RETURN TO MAIN MENU\n\n"

                                    "===========================\n"
                                    "=>"
                                ).lower().strip()
                    if InputF == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF LISTS ========\n\n"

                            "It's an ordered collection of items\n"
                            "that can store multiple values in a\n"
                            "single variable. Lists can contain\n"
                            "different data types (numbers,\n"
                            "strings, etc.) and can be changed\n"
                            "after creation.\n\n"

                            "=====================================\n"
                        )
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputF == 'b':
                        os.system('cls')
                        while True:
                            ListChoice = input(
                                        "===== LISTS IN PYTHON =====\n\n"

                                        "[A] SIMPLE LIST\n"
                                        "[B] NESTED LIST\n"
                                        "[C] LIST/ARRAY METHOD\n"                                                                   
                                        "[X] RETURN TO SUB MENU\n\n"

                                        "===========================\n"
                                    ).lower().strip()
                            
                            if ListChoice == 'a': # SIMPLE
                                os.system('cls')
                                while True:
                                    SimChoice = input(
                                    "====== SIMPLE LIST ======\n\n"

                                    "[A] DEFINITION\n"
                                    "[B] EXAMPLE\n"
                                    "[X] RETURN\n\n"

                                    "=========================\n\n"
                                    ).lower().strip()

                                    if SimChoice == 'a':
                                        os.system('cls')
                                        print(
                                        "===== DEFINITION OF SIMPLE LIST=====\n\n"

                                        "A simple list is a type of list\n"
                                        "that contains single, individual\n"
                                        "values only\n\n"

                                        "====================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue

                                    elif SimChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "========== EXAMPLE OF SIMPLE LIST ==========\n\n"

                                            "Input:\n"
                                            "\tfruits = [\"apple\",\"banana\",\"grapes\"]\n"
                                            "\tnumbers = [1,2,3,4,5]\n\n"

                                            "\tprint(fruits[0])\n"
                                            "\tprint(numbers[-1])\n\n"

                                            "Output:\n"
                                            "\tapple\n"
                                            "\t5\n\n"

                                            "============================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue
                                    
                                    elif SimChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue
                            
                            elif ListChoice == 'b': # NESTED
                                os.system('cls')
                                while True:
                                    NesChoice = input(
                                    "====== NESTED LIST ======\n\n"

                                    "[A] DEFINITION\n"
                                    "[B] EXAMPLE\n"
                                    "[X] RETURN\n\n"

                                    "=========================\n\n"
                                    ).lower().strip()

                                    if NesChoice == 'a':
                                        os.system('cls')
                                        print(
                                        "===== DEFINITION OF NESTED LIST=====\n\n"

                                        "A nested list is a list that\n"
                                        "contains one or more lists inside\n"
                                        "it.In other words, it is a list\n"
                                        "within a list.\n\n"
                                        
                                        "====================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue
                                    
                                    elif NesChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "========== EXAMPLE OF NESTED LIST ==========\n\n"

                                            "fruits = [[\"apple\",\"banana\",],[\"grapes\"]]\n"
                                            "numbers = [[1,2],[3,4],[5,6]]\n\n"

                                            "============================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue
                                    
                                    elif NesChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue

                            elif ListChoice == 'c': # LIST/ARRAY METHOD
                                os.system('cls')
                                while True:
                                    NesChoice = input(
                                    "=== LIST/ARRAY METHOD ===\n\n"

                                    "[A] DEFINITION\n"
                                    "[B] EXAMPLE\n"
                                    "[X] RETURN\n\n"

                                    "=========================\n\n"
                                    ).lower().strip()

                                    if NesChoice == 'a':
                                        os.system('cls')
                                        print(
                                        "===== DEFINITION OF LIST/ARRAY METHOD =====\n\n"

                                        "These are built-in functions that are used\n"
                                        "to add, remove, modify, or organize\n"
                                        "elements in a list\n\n."
                                        
                                        "===========================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue
                                    
                                    elif NesChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "========== EXAMPLE OF LIST/ARRAY METHOD ==========\n\n"

                                            ".append(item) - Adds an item to the end of the list\n"
                                            ".insert(index, item) - Adds an item at a specific position\n"
                                            ".extend(iterable) - Adds all items from another list or iterable\n"
                                            ".remove(item) - Removes the first occurrence of a value\n"
                                            ".pop(index) - Removes an item at a specific index (default is last)\n"
                                            ".clear() - Removes all items from the list\n"
                                            ".index(item) - Returns the index of the first occurrence\n"
                                            ".count(item) - Returns how many times an item appears\n"
                                            ".sort() - Sorts the list in ascending order\n"
                                            ".reverse() - Reverses the order of items\n"
                                            ".copy() - Returns a shallow copy of a list\n\n"

                                            "==================================================\n\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue
                                    
                                    elif NesChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue       

                            elif ListChoice == 'x':
                                os.system('cls')
                                print("Returning to SUB MENU!")
                                break

                            else:
                                os.system('cls')
                                print("Invalid Input.. Please Try Again..")
                                continue
                    
                    elif InputF == 'c':
                        codingactivity(
                            "For this activity we will use LISTS.\n"
                            "create a list like this [1,5,7,10,9]\n"
                            "then print the 2nd largest number",

                            "9",

                            "[1,5,7,10,9]"
                        )
                    elif InputF == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue
                continue
            
            elif user_inputs == 'g': #DICTIONARY
                os.system('cls')
                while True:
                    InputG = input(
                                    "===== DICTIONARY IN PYTHON =====\n\n"

                                    "[A] DEFINITION OF DICTIONARY\n"
                                    "[B] EXAMPLE OF DICTIONARY\n" 
                                    "[C] ACTIVITY\n"                                                                  
                                    "[X] RETURN TO MAIN MENU\n\n"

                                    "================================\n"
                                    "=>"
                                ).lower().strip()
                    
                    if InputG == 'a':
                        os.system('cls')
                        print(
                            "========== DEFINITION OF DICTIONARY ==========\n\n"

                            "A dictionary in Python is a data structure\n"
                            "that stores information in key-value pairs.\n"
                            "Each key has a value, and you use the key to\n"
                            "access the value.\n\n"

                            "==============================================\n\n"
                        )
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputG == 'b':
                        os.system('cls')
                        print(
                            "========== EXAMPLE OF DICTIONARY ==========\n\n"

                            "Input:\n"    
                            "Temperature = {\n"
                            "\t\"Key\":\"Value\",\n"
                            "\t\"Cold\":\"0-26 celsius\",\n"
                            "\t\"Neutral\":\"26-32 celsius\"\n"
                            "\t\"Hot\":\"32-45+ celsius\"\n"
                            "}\n\n"

                            "print(Temperature[\"Cold\"]\n\n)"

                            "Output:\n"
                            "0-26 celsius\n\n"

                            "===========================================\n\n"
                        )
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputG == 'c':
                        codingactivity(
                            "For this activity we will use DICTIONARY.\n"
                            "create a Dictionary list like this\n"
                            "{\"Red\":\"Apple\",\"Yellow\":\"Banana\",\"Blue\":\"Grapes}\n"
                            "the output must be 'Grapes'",

                            "Grapes",

                            '{"Red":"Apple","Yellow":"Banana","Blue":"Grapes"}'
                        )
                    elif InputG == 'x':
                        os.system('cls')
                        print("Returning to MAIN MENU!")
                        break

                    else:
                        os.system('cls')
                        print("Invalid Input.. Please Try Again..")
                        continue

            elif user_inputs == 'h': #FUNCTION
                os.system('cls')
                while True:
                    InputH = input(
                                    "===== FUNCTION IN PYTHON =====\n\n"

                                    "[A] DEFINITION OF FUNCTION\n"
                                    "[B] EXAMPLES OF FUNCTION\n"
                                    "[C] ACTIVITY\n"                                                                   
                                    "[X] RETURN TO MAIN MENU\n\n"

                                    "===========================\n"
                                    "=>"
                                ).lower().strip()
                    if InputH == 'a':
                        os.system('cls')
                        print(
                            "======== DEFINITION OF FUNCTION ========\n\n"

                            "A function in Python is a block of\n"
                            "reusable code that performs a specific\n"
                            "task. You can call the function whenever\n"
                            "you need it, instead of rewriting the\n"
                            "same code.\n\n"

                            "========================================\n"
                        )
                        input("Press ENTER to return to the menu...")
                        os.system('cls')
                        continue

                    elif InputH == 'b':
                        os.system('cls')
                        while True:
                            FunChoice = input(
                                "===== EXAMPLES OF FUNCTION =====\n\n"

                                "[A] BUILT-IN\n"
                                "[B] USER-DEFINED\n"
                                "[X] RETURN TO SUB MENU\n\n"

                                "================================\n\n"
                                ).lower().strip()
                            
                            if FunChoice == 'a': #BUILT IN
                                os.system('cls')
                                while True:
                                    BuiChoice = input(
                                        "====== BUILT-IN FUNCTIONS ======\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "================================\n\n"
                                        ).lower().strip()
                                    
                                    if BuiChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "======== DEFINITION OF BUILT-IN FUNCTION ========\n\n"

                                            "It's a function that is already provided by\n"
                                            "Python and can be used without creating or\n"
                                            "importing anything.\n\n"

                                            "=================================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue

                                    elif BuiChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "======== EXAMPLE OF BUILT-IN FUNCTION ========\n\n"

                                            "print() - displays output\n"
                                            "input() - gets user input\n"
                                            "int() - converts a value to an integer\n"
                                            "float() - converts a value to a floating-point number\n"
                                            "type() - shows the data type of a value\n\n"

                                            "==============================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue

                                    elif BuiChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue 
                                    
                            elif FunChoice == 'b': #USER DEFINED
                                os.system('cls')
                                while True:
                                    UseChoice = input(
                                        "====== USER-DEFINED FUNCTION ======\n\n"

                                        "[A] DEFINITION\n"
                                        "[B] EXAMPLE\n"
                                        "[X] RETURN\n\n"

                                        "====================================\n\n"
                                        ).lower().strip()
                                    
                                    if UseChoice == 'a':
                                        os.system('cls')
                                        print(
                                            "======== DEFINITION OF USER-DEFINED FUNCTION ========\n\n"

                                            "It's a function that is created by the programmer\n"
                                            "to perform a specific task\n\n"

                                            "=====================================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue

                                    elif UseChoice == 'b':
                                        os.system('cls')
                                        print(
                                            "======== EXAMPLE OF USER-DEFINED FUNCTION ========\n\n"

                                            "def greet():\n"
                                            "\tprint(\"Hello World\")\n\n"

                                            "==================================================\n"
                                        )
                                        input("Press ENTER to return to the menu...")
                                        os.system('cls')
                                        continue

                                    elif UseChoice == 'x':
                                        os.system('cls')
                                        print("Returning")
                                        break

                                    else:
                                        os.system('cls')
                                        print("Invalid Input.. Please Try Again..")
                                        continue 
                            
                            elif FunChoice == 'x':
                                os.system('cls')
                                print("Returning to SUB MENU!")
                                break

                            else:
                                os.system('cls')
                                print("Invalid Input.. Please Try Again..")
                                continue 
                    
                    elif InputH == 'c':
                        codingactivity(
                            "For this activity we will use FUNCTION specifically User-Defined.\n"
                            "Create a function named add_numbers that takes two parameters a and b.\n"
                            "Return the sum of a and b. Call the function and print the result using 3 and 2.\n"
                            "The Output must be 5",
                            "5",
                            "def"
                        )
                    elif InputH == 'x':
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
