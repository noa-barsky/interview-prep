def merge_sorted(lst1,lst2):
    combined = [0] * (len(lst1) + len(lst2))
    i = 0 
    j = 0
    k = 0 
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined[k] = lst1[i]
            i += 1
        else:
            combined[k] = lst2[j]
            j += 1
        k += 1
    while i < len(lst1):
        combined[k] = lst1[i]
        i +=1
        k += 1
    while  j < len(lst2):
        combined[k] = lst2[j]
        j += 1
        k += 1
    return combined 

print(merge_sorted([1,54,65,65,98,100], [54, 65,73]))