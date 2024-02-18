def positive_check(func):
    def wrapper(num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return func(num)
    return wrapper

@positive_check
def return_number(num):
    return num

number = int(input("Enter a positive number: "))

try:
    result = return_number(number)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

