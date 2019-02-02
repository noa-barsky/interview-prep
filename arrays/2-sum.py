def twoSum(l,k):
    numsSeenSoFar = set()
    for i in l:
        if (k - i) in numsSeenSoFar:
            return True
        numsSeenSoFar.add(i)
    return False
