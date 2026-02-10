def binary_search_with_bubble_sort(arr, target):
    original_arr = arr.copy()   # keep original array
    n = len(arr)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Binary Search
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return original_arr.index(target)  # return original index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


size = int(input("Enter number of elements in the list: "))
arr = []

for i in range(size):
    arr.append(int(input(f"Enter element {i+1}: ")))

target = int(input("Enter target value to search: "))

index = binary_search_with_bubble_sort(arr, target)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found (index -1)")
