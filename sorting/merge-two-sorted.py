def merge_sorted(lst1,lst2):
    combined = []
    i = 0 
    j = 0
    k = 0 
    while i < len(lst1) and j < len(lst):
        if lst1[i] > lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
        k + = 1
    while i < len(lst1):
        combined[k] = lst1[i]
        i + =1
        k += 1
    while  j < len(lst2):
        combined[k] =lst2[j]
        j + =1
        k += 1
    return combined 

print(merge_sorted([1,54,98,100], [54, 65,73]))