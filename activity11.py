temp = eval(input("Input the temperature inside the classroom here (In Celsius) \n==> "))
if temp <= 0:
  print("Freezing Temperature")
elif temp >= 1 and temp <= 20:
  print("Extremely Cole")
elif temp >= 21 and temp <= 30:
  print("Moderately Cold")
elif temp >= 31 and temp <= 37:
  print("Lukewarm")
elif temp >= 38 and temp <= 45:
  print("Hot")
elif temp >= 46 and temp <= 50:
  print("Boiling Hot")
elif temp >= 51:
  print("Dangerously Hot! Get out of there Immediately!")
else :
  print("error -..-1--.1-")
