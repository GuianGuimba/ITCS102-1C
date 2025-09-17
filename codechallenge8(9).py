import time
count = eval(input("⏳ COUNTDOWN TIMER SIMULATOR\nEnter the starting number for countdown ==> "))
print("Countdown Started!")
for n in range(count,0,-1):
    print(n)
    time.sleep(1)
print("Liftoff!")
