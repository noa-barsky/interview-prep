def alternatingCharacters(s):
    deletions = 0
    for i in range(0,len(s) - 1):
        if i == len(s) - 1:
            if s[i] == s[i-1]:
                deletions += 1
        else:
            if s[i] == s[i+1]:
                deletions += 1
            else:
                continue
    return deletions
            
print(alternatingCharacters("ABBA")) # ---> "ABA"