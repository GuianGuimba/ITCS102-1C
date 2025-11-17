import os
os.system('cls')

print("welcome to DLL Student Information System")
student_record = {}
while True:
    os.system('cls')
    print("Select from the options below\n" \
    "A - Add Student Record\n" \
    "B - Search Student Record\n" \
    "C - Edit Student Record\n" \
    "D - Delete Student Record\n" \
    "E - Print all Student Info\n" \
    "F - Export Data\n" \
    "G - Exit System\n")

    choice = input("Input your choice => ").lower().strip()
    if choice == 'a':
        print("Add Student Record")
        student_id = input("Input Student ID => ")
        first_name = input("Input Student First Name => ")
        last_name = input("Input Student Last Name => ")
        course = input("Input Student Course => ")
        section = input("Input Student Section => ")
        email = input("Input Student Email => ")
        student_record[student_id] = [first_name,last_name,course,section,email]
        print("Transfered Succesfully")
        continue
    
    elif choice == 'b':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("You have now exited the program")
        break
    else:
        print("Invalid Input, Try again...")
        continue
    
