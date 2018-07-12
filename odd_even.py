number=int(input())
if(number>=1 and number<=100000):
  if(number%2==0):
    print("Even")
  elif(number%2==1):
    print("Odd")
else:
  print("invalid")
