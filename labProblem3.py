import random
import time

def linearSearch(array, target):
    count = 0
    for i, value in enumerate(array):
        count += 1
        if value == target:
            return i, count
    return -1, count

def binarySearch(array, target):
    low, high, count = 0, len(array) - 1, 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if array[mid] == target:
            return mid, count
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count

def generateUsernames(n):
    usernames = [f'user{i}' for i in range(n)]
    random.shuffle(usernames)
    return usernames

def compareSearches():
    numUsernames = 100000
    usernames = generateUsernames(numUsernames)
    sortedUsernames = sorted(usernames)
    target = random.choice(usernames)

    # Linear Search
    startTime = time.perf_counter()
    linearIndex, linearCount = linearSearch(usernames, target)
    linearTime = time.perf_counter() - startTime

    # Binary Search
    startTime = time.perf_counter()
    binaryIndex, binaryCount = binarySearch(sortedUsernames, target)
    binaryTime = time.perf_counter() - startTime

    # Results
    print(f"Linear Search: Time = {linearTime:.6f} seconds, Comparisons = {linearCount}, Target Index = {linearIndex}, Target = {target}")
    print(f"Binary Search: Time = {binaryTime:.6f} seconds, Comparisons = {binaryCount}, Target Index = {binaryIndex}, Target = {target}")

if __name__ == "__main__":
    compareSearches()
