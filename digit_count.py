def digit_count_and_sum(n):
    if n < 0:
        n = -n

    count = 0
    total_sum = 0

    if n == 0:
        return 1, 0

    while n > 0:
        digit = n % 10
        total_sum += digit
        count += 1
        n //= 10

    return count, total_sum


num = int(input("Enter an integer: "))
count, digit_sum = digit_count_and_sum(num)

print("Digit count:", count)
print("Digit sum:", digit_sum)

