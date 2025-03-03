def find_max_min_dc(arr, left, right):
    """Finds max and min using Divide and Conquer"""
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min_left, max_left = find_max_min_dc(arr, left, mid)
    min_right, max_right = find_max_min_dc(arr, mid + 1, right)

    return min(min_left, min_right), max(max_left, max_right)


def find_max_min_normal(arr):
    """Finds max and min using Normal Iterative Approach"""
    minimum = maximum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum


def main():
    arr = list(map(int, input('Enter numbers: ').split()))
    choice = int(input("Enter choice:\n1. Divide and Conquer\n2. Normal Approach\n"))

    if choice == 1:
        minimum, maximum = find_max_min_dc(arr, 0, len(arr) - 1)
        print("Using Divide and Conquer:")
    elif choice == 2:
        minimum, maximum = find_max_min_normal(arr)
        print("Using Normal Approach:")
    else:
        print("Invalid choice!")
        return

    print(f'Minimum: {minimum}, Maximum: {maximum}')


# Execute main function
main()
