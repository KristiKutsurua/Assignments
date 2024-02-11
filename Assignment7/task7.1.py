def calculate_sum(input_list):
    total_sum = 0
    for element in input_list:
        total_sum += element
    return total_sum

list  = [100,20,30,50,5323,3321,22,56,700,90,10]
result = calculate_sum(list)
print(result)