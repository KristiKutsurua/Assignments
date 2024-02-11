total_sum = 0
while True:
    num = input("enter:\n")
    if num == 'sum':
          break
    if int(num) > 0:
            total_sum += int(num)


print(total_sum)