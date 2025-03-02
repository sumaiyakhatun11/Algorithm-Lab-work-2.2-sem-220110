def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def perform_sorting():
    n = int(input("Enter the number of elements: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))
    
    choice = input("Enter your choice (bubble/selection): ").lower()

    if choice == "bubble":
        bubble_sort(arr)
        print("Sorted array using Bubble Sort:", arr)
    elif choice == "selection":
        selection_sort(arr)
        print("Sorted array using Selection Sort:", arr)
    else:
        print("Invalid choice. Please enter 'bubble' or 'selection'.")

if __name__ == "__main__":
    perform_sorting()
