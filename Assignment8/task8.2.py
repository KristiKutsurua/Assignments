getOddElements = lambda numbers: list(map(lambda x: x, filter(lambda x: x % 2 != 0, numbers)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = getOddElements(numbers)
print(result)

