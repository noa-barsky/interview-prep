def reverse_str(s):
    start = len(s) - 1
    r_str = ""
    for c in range(start, -1 , - 1):
        r_str += s[c]
    return r_str
