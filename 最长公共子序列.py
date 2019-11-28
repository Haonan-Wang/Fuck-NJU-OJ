"""
最长公共子序列
Description

给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input

输入第一行为用例个数， 每个测试用例输入为两行，一行一个字符串


Output

如果没有公共子序列，不输出，如果有多个则分为多行，按字典序排序。
"""

str1, str2 = '', ''
d = {}
paths = set()


def dp(cur1, cur2):
    if (cur1, cur2) in d:
        return d[(cur1, cur2)]

    if cur1 == -1 or cur2 == -1:
        cur_d = 0
    elif str1[cur1] == str2[cur2]:
        cur_d = 1 + dp(cur1 - 1, cur2 - 1)
    else:
        cur_d = max([dp(cur1 - 1, cur2), dp(cur1, cur2 - 1)])

    d[(cur1, cur2)] = cur_d
    return cur_d


def getPaths(cur1, cur2, path):
    if d[(cur1, cur2)] == 0:
        paths.add(path)
        return

    if str1[cur1] == str2[cur2]:
        getPaths(cur1 - 1, cur2 - 1, str1[cur1] + path)
        return

    if d[(cur1 - 1, cur2)] == d[(cur1, cur2)]:
        getPaths(cur1 - 1, cur2, path)
    if d[(cur1, cur2 - 1)] == d[(cur1, cur2)]:
        getPaths(cur1, cur2 - 1, path)


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        str1, str2 = input(), input()
        cur1, cur2 = len(str1) - 1, len(str2) - 1

        d = {}
        dp(cur1, cur2)
        if d[(cur1, cur2)] == 0:
            continue

        paths = set()
        getPaths(cur1, cur2, '')
        paths = sorted(paths)
        for path in paths:
            print(path)
