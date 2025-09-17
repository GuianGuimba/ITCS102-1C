odd = 0
for n in range(1,11,1):
    numbers = eval(input("Input numbers here ==> "))
    if numbers % 2 != 0:
        odd += numbers
    
print("The sum of odd numbers you inputed is",odd)
