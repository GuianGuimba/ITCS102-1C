import os
import json
os.system('cls')


print("welcome to DLL Student Information System\n==============================")
student_record = {}
while True:
    #os.system('cls')
    print("Select from the options below\n" \
    "A - Add Student Record\n" \
    "B - Search Student Record\n" \
    "C - Edit Student Record\n" \
    "D - Delete Student Record\n" \
    "E - Print all Student Info\n" \
    "F - Export Data\n" \
    "G - Import Data\n" \
    "X - Exit System\n")

    choice = input("Input your choice => ").lower().strip()
    if choice == 'a': #Adding A Student Record
        os.system('cls')
        print("Add Student Record")
        student_id = input("Input Student ID => ").upper()
        first_name = input("Input Student First Name => ").upper()
        last_name = input("Input Student Last Name => ").upper()
        course = input("Input Student Course => ").upper()
        section = input("Input Student Section => ")
        email = input("Input Student Email => ")
        student_record[student_id] = [first_name,last_name,course,section,email]
        print("Transfered Succesfully")
        continue
    
    elif choice == 'b': #Searching A Student Record
        os.system('cls')
        print("Search Student Record")
        search = input("Input the Student ID you want to search => ").upper()
        for student_data in student_record.keys():
            if search in student_record.keys():
                print("RECORD FOUND\n====================")
                for id in student_record[search]:
                    print(f"- {id} -\n====================")
            else:
                print("RECORD NOT FOUND")
            break
        continue

    elif choice == 'c': #Editing A Student Record
        os.system('cls')
        print("Search Student Record")
        search = input("Input the Student ID you want to search => ").upper()
        for student_data in student_record.keys():
            if search in student_record.keys():
                print("RECORD FOUND\n====================")
                for id in student_record[search]:
                    print(f"- {id} -\n====================")
                    
                #New Value
                student_id = input("Input New Student ID => ").upper()

                first_name = input("Input New Student First Name => ").upper()
                last_name = input("Input New Student Last Name => ").upper()
                course = input("Input New Student Course => ").upper()
                section = input("Input New Student Section => ")
                email = input("Input New Student Email => ")

                #Transferring the new Value
                student_record[search][0] = first_name
                student_record[search][1] = last_name
                student_record[search][2] = course
                student_record[search][3] = section
                student_record[search][4] = email
                print("Record Succesfully Edited!")
            else:
                print("RECORD NOT FOUND")
                
                
            break
        continue
    elif choice == 'd': #Deleting A Student Record
        os.system('cls')
        print("Delete Student Record")
        search = input("Input the Student ID you want to Delete => ").upper()
        for student_data in student_record.keys():
            if search in student_record.keys():
                print("RECORD FOUND")
                for id in student_record[search]:
                    print(f"- {id} -")
                #Deleting A Record
                student_record.pop(search)
                print("Record Deleted..")

            else:
                print("RECORD NOT FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')
        print("Printing Student Records")
        for id,info in student_record.items():
            print(f"STUDENT ID - {id} - RECORD - {info}")

        continue
    elif choice == 'f': #Export Data / Saving
        print("EXPORTING DATA")
        with open('student_record.json','w') as new_file:
            json.dump(student_record, new_file, indent=4)
        
        print("DATA EXPORTED SUCCESFULLY")
        continue

    elif choice == 'g':
        print("IMPORTING DATA")
        with open('student_record.json','r') as new_file:
            imported_student = json.load(new_file)

        student_record = imported_student
        print("DATA IMPORTED SUCCESFULLY")
        continue
        
    elif choice == 'x':
        print("You have now exited the program")
        break
    else:
        print("Invalid Input, Try again...")
        continue
    
