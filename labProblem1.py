def findMaxMin(arr):
    if len(arr) == 0:
        return None, None  # Empty list edge case

    max_val = min_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    return max_val, min_val


def main():
    arr = list(map(int, input('Enter numbers: ').split()))
    max_val, min_val = findMaxMin(arr)
    if max_val is not None and min_val is not None:
        print(f'Max value: {max_val} and Min value: {min_val}')
    else:
        print('The array is empty.')


main()
