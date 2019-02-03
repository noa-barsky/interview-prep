def bubblesort(lst):
    for i in range(len(lst)):
        idx = i + 1
        for idx in range(len(lst)-1):
            if lst[idx] > lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp
    return lst

print(bubblesort([70, 60, 50, 40, 30]))