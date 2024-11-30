def binarySearch(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input and Execution
array = list(map(int, input("Enter numbers (space-separated): ").split()))
if not array:
    print("The array is empty! Please provide valid input.")
else:
    array.sort()
    key = int(input("Enter search key: "))
    result = binarySearch(array, key)

    if result != -1:
        print(f"Key found at index {result}.")
    else:
        print("Key not found.")
