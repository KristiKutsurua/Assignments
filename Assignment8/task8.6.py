def filter_by_ending(lst, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), lst))
        return filtered_list
    except TypeError as e:
        print(f"Error: {e}")
        return None

my_list = ['hello', 'world', 'coding', 'nod']
ending_string = 'ing'
result = filter_by_ending(my_list, ending_string)

if result is not None:
    print(result)