coins = []


def solve(amount):
    if amount == 0:
        return 0

    for coin in coins:
        if amount - coin >= 0:
            res = solve(amount - coin)
            if res != -1:
                return 1 + res

    return -1


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, amount = map(int, input().split())
        coins = list(map(int, input().split()))

        coins.sort(reverse=True)
        print(solve(amount))
