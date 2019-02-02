def bin_search(lst,n):
    middle = len(lst)//2
    if len(lst) == 1:
        if n == lst[0]:
            return True
        else:
            return False
    else: 
        if n == middle:
            return True
        elif n > lst[middle]:
            bin_search(lst[middle:],n)
        else:
            bin_search(lst[:middle],n)
    return False

