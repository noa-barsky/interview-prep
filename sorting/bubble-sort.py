def bubblesort(lst):
    for i in range(len(lst) - 1,0,-1):
        for idx in range(i):
            if lst[idx] > lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp
    return lst

