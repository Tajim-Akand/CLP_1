def find_max(a,b,c):
   if a>=b and a>=c:
       return a
   elif b>=a and b>=c:
       return b
   else:
       return c


num1 = (input("Enter the first value: "))
num2 = (input("Enter the second value: "))
num3 = (input("Enter the third value: "))


maximum = find_max(num1, num2,num3)
print("The Maximum value is: " ,maximum)
