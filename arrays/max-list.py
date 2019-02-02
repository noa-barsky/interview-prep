def max_lst(lst):
    my_max = lst[0]
    for i in lst:
        if i > my_max:
            my_max = i
    return my_max 
print(max_lst([453,1,42,3]))