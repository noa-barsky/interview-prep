def isBalanced(s):
    stack = []
    paran_match = {"(": ")", "[":"]", "{":"}" }
    open_paran = ["(", "{", "["]
    close_paran = [")", "}", "]"]
    for p in s:
        if p in open_paran:
            stack.append(p)
        else:
            if not stack:
                return "NO"
            else:
                recent = stack.pop()
                if paran_match[recent] == p:
                    continue
                else:
                    return "NO"
    if stack == []:
        return "YES"
    else:
        return "NO"