p, q = 0, 0


def fill(x, y, n, a, b):
    if n == 0:
        return None

    half = int(pow(2, n - 1))
    mid_x = x + half
    mid_y = y + half

    params = [
        [x, y, mid_x - 1, mid_y - 1],
        [x, mid_y, mid_x - 1, mid_y],
        [mid_x, mid_y, mid_x, mid_y],
        [mid_x, y, mid_x, mid_y - 1]
    ]

    if a < mid_x:
        if b < mid_y:
            pos = 0
        else:
            pos = 1
    else:
        if b < mid_y:
            pos = 3
        else:
            pos = 2

    res = []
    for i in range(len(params)):
        if i == pos:
            params[pos][2:] = [a, b]
            continue

        _, _, _a, _b = params[i]
        if _a == p and _b == q:
            continue

        res.append([_a, _b])
    if len(res) == 2:
        return res

    for _x, _y, _a, _b in params:
        res = fill(_x, _y, n - 1, _a, _b)
        if res is not None:
            return res

    return None


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, a, b = map(int, input().split())
        p, q = map(int, input().split())

        res = fill(0, 0, n, a, b)
        if res[0][0] > res[1][0] or (res[0][0] == res[1][0] and res[0][1] > res[1][1]):
            res[0], res[1] = res[1], res[0]
        print(','.join([' '.join(map(str, coord)) for coord in res]))
