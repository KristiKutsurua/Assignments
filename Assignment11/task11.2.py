def combine_and_remove_duplicates(tuple1, tuple2):
    combined_tuple = tuple(set(tuple1).union(set(tuple2)))
    duplicated_values = list(set(element for element in combined_tuple if (tuple1 + tuple2).count(element) > 1))

    print("combined_tuple:", combined_tuple)
    print("duplicated_values:", duplicated_values)

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combine_and_remove_duplicates(tuple1, tuple2)
