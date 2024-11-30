def mergeSort(array):
    if len(array) > 1:
        leftArray = array[:len(array)//2]
        rightArray = array[len(array)//2:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = 0
        j = 0
        k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1

def main():
    array = list(map(int, input('Enter unsorted numbers: ').split()))
    mergeSort(array)
    print('Sorted numbers: ', array)

main()
