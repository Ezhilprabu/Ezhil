n=int(input())
if(n>0 and n<=1000):
  if(n%1==0 and n%n==0):
    print("yes")
  else:
    print("no")
else:
  print("no")
