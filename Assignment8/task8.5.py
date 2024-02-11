from functools import reduce

def multiplyNumbers(numbers):
    try:
        result = reduce(lambda x, y: x * y, map(int, numbers))
        return result
    except ValueError:
        raise TypeError("Invalid input. Please provide a list of strings.")
    

list = [1, 2, 3, 4, 'a']

try:
    output = multiplyNumbers(list)
    print(output)
except TypeError as e:
    print(e)