a = int(input())

b = int(input())

c = int(input())

if a >= b and a >= c:

    max_val = a

elif b >= a and b >= c:

    max_val = b

else:

    max_val = c

print("Maximum:", max_val)