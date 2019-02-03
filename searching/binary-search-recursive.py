def binary_search(arr,ele):
    
    # Base Case!
    if len(arr) == 0:
        return False 
    # Recursive Case
    else:
        mid = len(arr) // 2
        # If match found
        if arr[mid] == ele:
            return True   
        # Call again on second half
        elif ele < arr[mid]:
            return binary_search(arr[:mid],ele)
        # Or call on first half
        else:
            return binary_search(arr[mid + 1:],ele)


print(binary_search([1,2,3,4,5], 8))