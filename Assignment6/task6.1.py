def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

str1 = str(input("შეიყვანეთ პირველი სიტყვა:\n"))
str2 = str(input("შეიყვანეთ მეორე სიტყვა:\n"))

result = anagram(str1, str2)
print(result)