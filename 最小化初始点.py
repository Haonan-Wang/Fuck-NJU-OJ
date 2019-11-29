"""
最小化初始点

Description

给定一个网格，其中每个像元由正，负或无点组成，即零点。 仅当我们有正点（> 0）时，我们才能跨单元格移动。 每当我们经过一个单元格时，该单元格中的点都会添加到我们的总体点中。 我们需要遵循以下某些规则来找到从（0，0）到达像元（m-1，n-1）的最小初始点：

1.从一个单元格（i，j）我们可以移至（i + 1，j）或（i，j + 1）。

2.如果您在（i，j）的总点小于等于0，我们将无法从（i，j）移开。

3.我们必须通过最小正点达到（n-1，m-1），即 i.e., > 0。


Input

第一行包含一个整数T，表示测试用例的总数。在每个测试用例中，第一行包含两个整数R和C，表示数组的行数和列数。
第二行包含一行的值，即网格，在单行中由行主要顺序中的空格分隔。

约束:

1 ≤ T ≤ 30

1 ≤ R,C ≤ 10

-30 ≤ A[R][C] ≤ 30

Input: points[m][n] = { {-2, -3, 3},
{-5, -10, 1},
{10, 30, -5}
};


Output

打印最小的初始点以在单独的行中到达最右下角的单元格。

7

说明：
7是到达目的地的最小值
积极的道路。 下面是路径。

（0,0）->（0,1）->（0,2）->（1，2）->（2，2）

我们从（0，0）开始于7，我们到达（0，1）
与5，（0，2）与2，（1，2）与5，（2，2）与，最后我们得到1点（我们需要
最后大于0分）。


Sample Input 1

1
3 3
-2 -3 3 -5 -10 1 10 30 -5
Sample Output 1

7
"""

import math


points = []
r, c = 0, 0
d = {}


def dp(i, j):
    if (i, j) in d:
        return d[(i, j)]

    point = points[i * c + j]
    min_point = math.inf
    if i < r - 1:
        min_point = min(dp(i + 1, j), min_point)
    if j < c - 1:
        min_point = min(dp(i, j + 1), min_point)
    if min_point == math.inf:
        min_point = 1
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
