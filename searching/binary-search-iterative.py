def binary_search(arr,ele):
    
    # First and last index values
    first = 0
    last = len(arr) - 1    
    while first <= last:
        
        mid = (first + last) // 2 # or // for Python 3
        
        # Match found
        if arr[mid] == ele:
            return True
        
    # Set new midpoints up or down depending on comparison
        # Set down
        elif ele < arr[mid]:
            last = mid - 1
        # Set up 
        else:
            first = mid + 1
                
    return False


print(binary_search([1,2,3,4,5], 5))