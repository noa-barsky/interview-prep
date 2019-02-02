def sum_lst(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_lst(lst[1:])

print(sum_lst([1,2,3]))