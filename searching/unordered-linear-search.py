def seq_search(arr,ele):
    for i in arr:
        if i == ele:
            return True
    return False

print(seq_search([43,123,12,1], 85))