def isBalanced(s):
    stack = []
    paran_match = {"(": ")", "[":"]", "{":"}" }
    for p in s:
        if p in paran_match:
            stack.append(p)
        else:
            if not stack:
                return False
            else:
                recent = stack.pop()
                if paran_match[recent] != p:
                    return False
    if stack == []:
        return True
    return False

print(isBalanced("{{[]}}"))