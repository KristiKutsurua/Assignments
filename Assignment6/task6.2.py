def charInString(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1

    return count
   

string = str(input("შეიყვანეთ სტრიქონი:\n"))
char = str(input("შეიყვანეთ სიმბოლო:\n"))

result = charInString(string, char)
print(result)
