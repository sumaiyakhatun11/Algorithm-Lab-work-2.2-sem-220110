def quickSort(arr, left, right):
    if left < right:
        partitionPos = partitionArr(arr, left, right)
        quickSort(arr, left, partitionPos-1)
        quickSort(arr, partitionPos+1, right)

def partitionArr(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

def main():
    arr = list(map(int, input('Enter numbers: ').split()))
    quickSort(arr, 0, len(arr) - 1)
    print('Sorted array is: ', arr)

main()
