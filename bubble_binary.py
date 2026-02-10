arr = list(map(int, input().split()))

target = int(input())

# bubble sort

for i in range(len(arr)):

    for j in range(len(arr) - i - 1):

        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# binary search

left = 0

right = len(arr) - 1

index = -1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:

        index = mid

        break

    elif arr[mid] < target:

        left = mid + 1

    else:

        right = mid - 1

print("Index:", index)