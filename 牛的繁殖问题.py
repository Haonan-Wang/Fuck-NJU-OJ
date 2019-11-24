mod = 1000000007
d = {0: 0, 1: 1, 2: 1}


def fib(n):
    if n < 3:
        return d[n]

    if n in d:
        return d[n]

    if (n % 2 == 1):
        k = (n + 1) // 2
        x = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % mod
        if x < 0:
            x += mod
        d[n] = x

    else:
        k = n // 2
        x = (fib(k) * ((fib(k + 1) * 2) - fib(k))) % mod
        if x < 0:
            x += mod
        d[n] = x
    return d[n]


if __name__ == "__main__":
    case = int(input())
    while case:
        n = int(input())
        print(fib(n + 1))
        case -= 1
