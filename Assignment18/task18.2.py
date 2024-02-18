class PositiveCheck:
    def __init__(self, func):
        self.func = func

    def __call__(self, num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return self.func(num)

@PositiveCheck
def return_number(num):
    return num

try:
    num = int(input("Enter a positive number: "))
    result = return_number(num)
    print("Returned number:", result)
except ValueError as ve:
    print(ve)
