def alternatingCharacters(s):
    deletions = 0
    new_str = ""
    for i in range(0,len(s)):
        if i == len(s) - 1:
            if s[i] == s[i-1]:
                deletions += 1
            else:
                new_str += s[i]    
        else:
            if s[i] == s[i+1]:
                
                deletions += 1
            else:
                new_str += s[i]
    return deletions,new_str
            
print(alternatingCharacters("ABBCCA")) # ---> "ABCA"