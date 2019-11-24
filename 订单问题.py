N, X, Y = 0, 0, 0
A, B = [], []

d = {}


def dp(cur, i, j):
    if cur == N:
        return 0
    if (cur, i, j) in d:
        return d[(cur, i, j)]

    max_tip = 0
    if i < X:
        max_tip = max([A[cur] + dp(cur + 1, i + 1, j), max_tip])
    if j < Y:
        max_tip = max([B[cur] + dp(cur + 1, i, j + 1), max_tip])

    d[(cur, i, j)] = max_tip
    return max_tip


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        N, X, Y = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        d = {}
        print(dp(0, 0, 0))
