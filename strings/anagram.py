def anagram(a,b):
    dict_a ={}
    dict_b = {}
    for c in a:
        dict_a[c] = a.count(c)
    for c in b:
        dict_b[c] = b.count(c)
    return dict_a == dict_b