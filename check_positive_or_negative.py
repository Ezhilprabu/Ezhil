number=int(input())
if(number>=1 and number<=100000):
	print("Positive")
elif(number==0):
	print("Zero")
elif(number<0):
	print("Negative")
else:
	print("Not in Range")
