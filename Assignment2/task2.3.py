num1 = int(input("შეიყვანეთ პირველი რიცხვი:\n"))
num2 = int(input("შეიყვანეთ მეორე რიცხვი:\n"))
operator = str(input("შეიყვანეთ ოპერატორი:\n"))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '//':
    print(num1 // num2)
elif operator == '%':
    print(num1 % num2)
elif operator == '**':
    print(num1 ** num2)
