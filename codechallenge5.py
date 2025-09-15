factorial = eval(input("Please input 1 number ==> "))
sum = 1
for x in range(factorial,0,-1):
    sum *= x
print("The factorial of",factorial,"is",sum)
