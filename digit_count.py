n = int(input())

n = abs(n)

count = 0

total = 0

if n == 0:

    count = 1

else:

    while n > 0:

        total += n % 10

        count += 1

        n //= 10

print("Digits:", count)

print("Sum:", total)