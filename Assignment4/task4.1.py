text = str(input("შეიყვანეთ ტექსტი:\n"))
palyndrome = True

for i in range(0, int(len(text)/2)):
    if text[i] != text[len(text)-i-1]:
            palyndrome = False
    else:
          palyndrome = True

if palyndrome:
      print("შეყვანილი ტექსტი არის პალინდრომი")
else:
      print("შეყვანილი ტექსტი არ არის პალინდრომი")