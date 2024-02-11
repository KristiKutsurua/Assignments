my_llist = [43, '22', 12, 66, 210, "hi"]

#a
print(my_llist.index(210))

#b
my_llist[5] = my_llist[5] + "hello"

#c
my_llist.pop(2)
print(my_llist)

#d
my_llist_2 = my_llist.copy()
my_llist_2.clear()
print(my_llist, my_llist_2)

