def count_items(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

def is_anagram(a, b):
    return count_items(a) == count_items(b)

print(is_anagram("aabc", "caba"))