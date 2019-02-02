def len_lst(lst):
    length = 0
    for element in lst:
        length += 1
    return length

def sum_lst(lst):
    total = 0
    for element in lst:
        total += element
    return total

print(len_lst([1,2,3]))
print(sum_lst([1,2,3]))