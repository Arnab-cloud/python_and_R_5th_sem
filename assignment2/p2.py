lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
lst_lst = [list(tup) for tup in lst_tuples]
print("Before", lst_tuples)
print("After", lst_lst)