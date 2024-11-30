def maxMinDivideConquer(arr, low, high, count):
    if low == high:  # Single element
        count += 1
        return arr[low], arr[low], count
    elif high == low + 1:  # Two elements
        count += 2
        if arr[low] > arr[high]:
            return arr[low], arr[high], count
        else:
            return arr[high], arr[low], count

    # Divide the array into halves
    mid = (low + high) // 2
    leftMax, leftMin, count = maxMinDivideConquer(arr, low, mid, count)
    rightMax, rightMin, count = maxMinDivideConquer(arr, mid + 1, high, count)

    # Combine results
    finalMax = max(leftMax, rightMax)
    finalMin = min(leftMin, rightMin)
    count += 2
    return finalMax, finalMin, count


# Input and execution
numbers = list(map(int, input("Enter numbers: ").split()))
if not numbers:
    print("The array is empty! Please enter valid numbers.")
else:
    count = 0
    maxValue, minValue, totalCount = maxMinDivideConquer(numbers, 0, len(numbers) - 1, count)
    print(f"Max value: {maxValue}, Min value: {minValue}, Steps (Order of n): {totalCount}")
