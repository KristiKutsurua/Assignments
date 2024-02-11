def calculate(num1, num2, operator):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '%': lambda x, y: x % y if y != 0 else None,
        '**': lambda x, y: x ** y,
    }

    if operator in operators:
        return operators[operator](num1, num2)
    else:
        return "Invalid operator"


num1 = float(input("შეიყვანეთ პირველი რიცხვი: \n"))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: \n"))
operator = input("შეიყვანეთ ოპერატორი: \n")

result = calculate(num1, num2, operator)
print("Result:", result)
