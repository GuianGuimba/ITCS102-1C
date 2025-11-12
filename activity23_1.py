def another(name):
    print(f"hello my name is{name}")

def NLA(name,location,age):
    print(f"Their name is {name}, From {location}, age of {age}")

def Return(number):
    sum = 0
    for x in range(1,number+1,1):
        sum += x
    return sum

def Factorial(number):
    factorial = 1
    for x in range(number,0,-1):
        factorial *= x
    return factorial
