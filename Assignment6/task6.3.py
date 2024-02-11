def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, " ")
        a, b = b, a + b

    

n = int(input("შეიყვანეთ რიცხვი:\n"))

result = fibonacci(n)
print(result)
