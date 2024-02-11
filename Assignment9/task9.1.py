import random

def generate_sorted_lists():
    random_numbers = [random.randint(1, 1000) for _ in range(100)]

    increasing_list = sorted(random_numbers)

    decreasing_list = sorted(random_numbers, reverse=True)

    return increasing_list, decreasing_list


increasing, decreasing = generate_sorted_lists()

print("Increasing List:", increasing)
print("Decreasing List:", decreasing)