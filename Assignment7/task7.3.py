def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

word  = str(input("შეიყვანეთ სიტყვა: \n"))
result = reverse_string(word)
print(result)