is_multiple_of_three = lambda x: x % 3 == 0


def find_three_multiples_indexes(input_list, input_lambda):
    result_list = []

    for index, value in enumerate(input_list):
        if input_lambda(value):
            result_list.append(index)

    return result_list

input_numbers = [1, 3, 5, 6, 9, 12, 15, 18, 21]
result_indexes = find_three_multiples_indexes(input_numbers, is_multiple_of_three)


print("Indexes of Three Multiples:", result_indexes)