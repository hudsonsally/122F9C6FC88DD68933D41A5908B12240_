def oddeven(a):
  if(a%2==0):
    return 1
  else:
    return 0
a=int(input("Enter a number ="))
if(oddeven(a)==1):
  print("The given number is even")
elif(oddeven(a)==0):
   print("The given number is odd")