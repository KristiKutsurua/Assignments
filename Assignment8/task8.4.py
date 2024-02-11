strings = ["level", "python", "radar", "hello", "madam"]

palindrome = list(map(lambda s: s == s[::-1], filter(lambda s: True, strings)))

print(palindrome)