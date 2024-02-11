nums = [1, 2, 3]
chars = ['a', 'b', 'c']

def groupLists(list1, list2): 
    result = [f"({num}, '{letter}')" for num, letter in zip(list1, list2)]
    
    return result


result = groupLists(nums, chars)
print(result)