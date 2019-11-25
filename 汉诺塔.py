def func(n, fro, buf, to):
    if (n == 1):
        return 2

    step = 0
    step += func(n - 1, fro, buf, to)
    step += 1
    step += func(n - 1, to, buf, fro)
    step += 1
    step += func(n - 1, fro, buf, to)
    return step


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        print(func(n, 'a', 'b', 'c'))
        