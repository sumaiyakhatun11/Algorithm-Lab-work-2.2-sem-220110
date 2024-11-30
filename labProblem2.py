def binarySearch(array, target):
    low, high, stepCount = 0, len(array) - 1, 0

    while low <= high:
        stepCount += 1
        mid = (low + high) // 2
        if array[mid] == target:
            return mid, stepCount
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, stepCount


def main():
    print("\nMenu:")
    print("1. Average Case (target exists in the array)")
    print("2. Worst Case (target does not exist in the array)")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice not in [1, 2]:
            print("Invalid choice! Exiting...")
            return
    except ValueError:
        print("Invalid input! Exiting...")
        return

    try:
        array = list(map(int, input("Enter a sorted array (space-separated): ").split()))
        if not array:
            print("The array is empty! Exiting...")
            return
    except ValueError:
        print("Invalid array input! Exiting...")
        return

    array.sort()
    target = int(input("Enter the target element: "))

    if choice == 2 and target in array:
        print("Warning: For worst case, the target should not be in the array!")

    index, stepCount = binarySearch(array, target)

    if index != -1:
        print(f"Target found at index {index}.")
    else:
        print("Target not found in the array.")
    print(f"Total loop iterations: {stepCount}")


if __name__ == "__main__":
    main()
