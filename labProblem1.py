import time

def findMaxMinLinear(array):
    maxValue, minValue, stepCount = array[0], array[0], 0
    for num in array[1:]:
        stepCount += 1
        maxValue, minValue = max(maxValue, num), min(minValue, num)
    return maxValue, minValue, stepCount

def findMaxMinDivideAndConquer(array, low, high, stepCount):
    if low == high:
        return array[low], array[low], stepCount + 1
    if high == low + 1:
        stepCount += 1
        return (array[low], array[high], stepCount + 1) if array[low] > array[high] else (array[high], array[low], stepCount + 1)
    mid = (low + high) // 2
    leftMax, leftMin, stepCount = findMaxMinDivideAndConquer(array, low, mid, stepCount)
    rightMax, rightMin, stepCount = findMaxMinDivideAndConquer(array, mid + 1, high, stepCount)
    return max(leftMax, rightMax), min(leftMin, rightMin), stepCount + 2

def main():
    while True:
        choice = input('\nMenu:\n1. Linear Search\n2. Divide & Conquer\n3. Exit\nEnter choice (1-3): ')
        if choice == '3':
            print('Exiting... Thank you!')
            break
        if choice not in ['1', '2']:
            print('Invalid choice! Please try again.')
            continue

        try:
            array = list(map(int, input('Enter numbers separated by spaces: ').split()))
            if not array:
                print("The list is empty! Please provide valid input.")
                continue
        except ValueError:
            print("Invalid input! Please enter only numbers.")
            continue

        startTime = time.perf_counter()
        if choice == '1':
            maxValue, minValue, stepCount = findMaxMinLinear(array)
        else:
            maxValue, minValue, stepCount = findMaxMinDivideAndConquer(array, 0, len(array) - 1, 0)
        elapsedTime = time.perf_counter() - startTime
        print(f'Max: {maxValue}, Min: {minValue}, Time: {elapsedTime:.6f}s, Steps: {stepCount}')

if __name__ == '__main__':
    main()
