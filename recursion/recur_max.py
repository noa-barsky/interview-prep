

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = find_max(lst[1:])
        return m if m > lst[0] else lst[0]



print(find_max([1,2,3,5]))