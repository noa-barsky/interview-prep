def fib_sum_iter(n):
    a, b = 0, 1
    total = 0
    for i in range(0, n):
        a, b = b, a + b
        total += a
    return total

def fib_sum_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_sum_recur(n - 1) + fib_sum_recur(n - 2) + 1

print(fib_sum_recur(4))