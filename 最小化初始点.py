import math


points = []
r, c = 0, 0
d = {}


def dp(i, j):
    if (i, j) in d:
        return d[(i, j)]

    point = points[i * c + j]
    if i == r - 1 and j == c - 1:
        if point >= 0:
            min_point = 1
        else:
            min_point = 1 - point
        d[(i, j)] = min_point
        return min_point

    min_point = math.inf
    if i < r - 1:
        min_point = min(dp(i + 1, j), min_point)
    if j < c - 1:
        min_point = min(dp(i, j + 1), min_point)
    min_point = max(1, min_point - point)

    d[(i, j)] = min_point
    return min_point


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        r, c = map(int, input().split())
        points = list(map(int, input().split()))

        d = {}
        print(dp(0, 0))
