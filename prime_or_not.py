n=int(input())
if(n>0 and n<=1000):
  for i in range(2,n):
    if(n%i==0):
      print("yes")
    else:
      print("no")
else:
  print("no")
