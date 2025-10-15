name = input("Hello, What is your name? ")
print("\n================================================\n" \
"ODD NUMBER SELECTOR, Press 0 to stop the loop\n"
"================================================\n")
Loop = True
sum = 0
odd = " "

while Loop == True:
    number = eval(input("Input a Random number here ==>"))
    if number %2 == 1:
        print("ODD NUMBER DETECTED")
        sum += number
        odd += str(number) + " "
        continue
    elif number == 0:
        print("Stopping....")
        break
    else:
        if number %2 == 0:
            print("EVEN NUMBER DETECTED")
            continue
        else:
            print("Invalid")
            continue

print(f"Hi {name}, the sum of all ODD numbers is {sum}\nGODD numbers include the ff =>{odd}")
