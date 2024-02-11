def calculate_sum(num):
    if num < 10:
        return num
    else:
        return num % 10 + calculate_sum(num // 10)

num  = int(input("შეიყვანეთ რიცხვი: \n"))
result = calculate_sum(num)
print(result)