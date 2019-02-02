def rotate_left(lst, n):
    return lst[n:] + lst[:n]

def rotate_right(lst,n):
    return lst[-n:] + lst[:-n]
print(rotate_left([1,2,3,4,5], 1) )
print(rotate_right([1,2,3,4,5], 1) )