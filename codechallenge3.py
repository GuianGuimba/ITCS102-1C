name = input("What is your name?")
fare = eval(input("How much is you fare fee?"))
student = input("Are you a student? Yes or No?")

a = fare * 0.2
A = fare - a

if student.lower() == "yes" :
	print("Hello",name,"Since you are a student are a given a 20% discount for your fare fee!",fare,">",A)
else :
	print("Sorry!",name, "Since you are not a student you will be given full price..")
