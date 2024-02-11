import random

def generate_random_numbers():
    return [random.randint(1, 1000) for _ in range(100)]

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(sorted_arr, target):
    low, high = 0, len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = sorted_arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

random_numbers = generate_random_numbers()
target_value = random.choice(random_numbers)

linear_search_result = linear_search(random_numbers, target_value)
print(f"Linear Search: Target {target_value} {'found' if linear_search_result != -1 else 'not found'} at index {linear_search_result}")

bubble_sort(random_numbers)
binary_search_result = binary_search(random_numbers, target_value)
print(f"Binary Search: Target {target_value} {'found' if binary_search_result != -1 else 'not found'} at index {binary_search_result}")
