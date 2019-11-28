"""
点的凸包
Description

Convex Hull of a set of points, in 2D plane, is a convex polygon with minimum area such that each point lies either
on the boundary of polygon or inside it. Now given a set of points the task is to find the convex hull of points.
一组点的凸包在2D平面中是具有最小面积的凸多边形，使得每个点位于多边形的边界上或内部。 现在给定一组点，任务是找到点的凸包。

Input

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case
contains an integer N denoting the no of points. Then in the next line are N*2 space separated values denoting the
points ie x and y.Constraints:1<=T<=100,1<=N<=100,1<=x,y<=1000


Output

For each test case in a new line print the points x and y of the convex hull separated by a space in sorted order
(increasing by x) where every pair is separated from the other by a ','. If no convex hull is possible print -1.


Sample Input 1

2
3
1 2 3 1 5 6
3
1 2 4 4 5 1
Sample Output 1

1 2, 3 1, 5 6
1 2, 4 4, 5 1
"""


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
