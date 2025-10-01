number = eval(input("MULTIPLICATION TABLE MAKER\nEnter a Number ==> "))
print("Multiplication for",number,"is..")
for n in range(1,11,1):
    x = number * n
    print(number,"x",n,"=",x)
