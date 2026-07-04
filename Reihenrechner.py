def a(n):
    return 2 ** (n - 1)


def s(n):
    k = 1
    s = 0
    while k <= n:
        s += a(k)
        k += 1
    return s


n = 1
while n <= 5:
    print("s_", n, " = ", s(n))
    n += 1
