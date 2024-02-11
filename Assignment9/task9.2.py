import random

def generate_random_numbers(n=100):
    return [random.randint(1, 1000) for _ in range(n)]

def bubble_sort(arr, increasing=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if increasing:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr, increasing=True):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if increasing:
                if arr[j] < arr[min_idx]:
                    min_idx = j
            else:
                if arr[j] > arr[min_idx]:
                    min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

random_numbers = generate_random_numbers()

bubble_sorted_increasing = bubble_sort(random_numbers.copy(), increasing=True)
print("Increasing Bubble Sort:", bubble_sorted_increasing)

selection_sorted_decreasing = selection_sort(random_numbers.copy(), increasing=False)
print("Decreasing Selection Sort:", selection_sorted_decreasing)
