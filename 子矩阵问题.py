"""
子矩阵问题

Description

给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。


Input

输入第一行为测试用例个数。每一个用例有若干行，第一行为矩阵行数n和列数m，下面的n行每一行是用空格隔开的0或1。


Output

输出一个数值。


Sample Input 1

1
3 4
1 0 1 1
1 1 1 1
1 1 1 0
Sample Output 1

6
"""

def cal_max_rect(heights):
    s = []
    max_rect = 0
    heights.append(-1)
    for i in range(len(heights)):
        while s and heights[i] <= heights[s[-1]]:
            top = s.pop(-1)
            if s:
                begin = s[-1]
            else:
                begin = -1
            width = i - begin - 1
            max_rect = max([max_rect, heights[top] * width])
        s.append(i)
    return max_rect


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        m, n = map(int, input().split())
        nums = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            row = list(map(int, input().split()))
            for j in range(n):
                nums[i][j] = row[j]

        ans = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max([cal_max_rect(heights), ans])
        print(ans)
