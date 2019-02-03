def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    
    for i in nums:
        if i in aux_dict:
            return True
        else:
            aux_dict[target - i] = 1
    return False
print(two_sum([1,2,3,4,4], 34))