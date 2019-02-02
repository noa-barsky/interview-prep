def hanoi(n, origin, destination, temporary):
    if n > 0:
        pre = hanoi(n-1,origin, temporary, destination)
        print("moved from ",origin," to ", destination)
        post = hanoi(n-1, temporary, destination, origin)
        return pre + post + 1
    else:
        return 0

print(hanoi(3, "A", "C", "B" ))