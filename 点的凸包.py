import functools


n = 0
p, ans, visit = [], [], []


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cmp(a, b):
    if a.x != b.x:
        return a.x - b.x
    else:
        return a.y - b.y


def Djudge(a1, a2, a3):
    calculate = a1.x * a2.y + a3.x * a1.y + a2.x * a3.y - a3.x * a2.y - a2.x * a1.y - a1.x * a3.y
    return calculate


def DealLeft(first, last):
    maxv, index = 0, -1
    i = first

    if first < last:
        for i in range(first + 1, last):
            calcu = Djudge(p[first], p[i], p[last])
            if calcu == 0:
                visit[i] = 1
            if calcu > maxv:
                maxv = calcu
                index = i
    else:
        while i > last:
            calcu = Djudge(p[first], p[i], p[last])
            if calcu == 0:
                visit[i] = 1
            if calcu > maxv:
                maxv = calcu
                index = i
            i -= 1

    if index != -1:
        visit[index] = 1
        DealLeft(first, index)
        DealLeft(index, last)


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        p, ans, visit = [], [], [0] * n
        for i in range(n):
            p.append(Point(nums[2 * i], nums[2 * i + 1]))
            ans.append(Point(0, 0))

        p.sort(key=functools.cmp_to_key(cmp))
        visit[0] = 1
        visit[n - 1] = 1
        DealLeft(0, n - 1)
        DealLeft(n - 1, 0)

        t = 0
        for i in range(n):
            if visit[i] == 1:
                ans[t].x = p[i].x
                ans[t].y = p[i].y
                t += 1

        points = [' '.join([str(point.x), str(point.y)]) for point in ans[:t]]
        print(', '.join(points))
