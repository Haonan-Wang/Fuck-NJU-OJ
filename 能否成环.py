"""
Description

Given an array of strings A[ ], determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first character of Y.
If every string of the array can be chained, it will form a circle. For example,
for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf".


描述

给定字符串A []的数组，确定字符串是否可以链接在一起形成一个圆。 如果X的最后一个字符与Y的第一个字符相同，则字符串X可以与另一个字符串Y链接在一起
如果数组的每个字符串都可以链接，它将形成一个圆。 例如，对于数组arr [] = {“ for”，“ geek”，“ rig”，“ kaf”}，答案将是“是”，因为给定的字符串可以链接为“ for”，“ rig”，“ geek” ”和“ kaf”。


Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.

The first line of each test case contains a positive integer N, denoting the size of the array.

The second line of each test case contains a N space seprated strings, denoting the elements of the array A[ ].

1 <= T

0 < N

0 < A[i]


Output

If chain can be formed, then print 1, else print 0.


Sample Input 1 

2
3
abc bcd cdf
4
ab bc cd da


Sample Output 1

0
1
"""


from collections import defaultdict


def dfs(graph, start, visited, stack):
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited, stack)
    stack.append(start)


def reverse_graph(graph):
    edges = []
    for k, val in graph.items():
        for node in val:
            edges.append((k, node))

    rev = defaultdict(list)
    for u, v in edges:
        rev[v].append(u)

    return rev


def dfs_r(graph, start, visited, store):
    visited.add(start)
    store.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited, store)


def kosaraju(graph, n):
    visited = set()
    stack = []
    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited, stack)

    rev = reverse_graph(graph)

    visited = set()
    out = []
    while stack:
        node = stack.pop()
        temp = []
        if node not in visited:
            dfs_r(rev, node, visited, temp)
            out.append(temp)

    return out


T = int(input())
for _ in range(T):
    n = int(input())
    arr = input().strip().split(' ')

    if n == 1:
        st = arr[0]
        if st[0] == st[-1]:
            print(1)
        else:
            print(0)
    else:
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if arr[i][-1] == arr[j][0]:
                    graph[i].append(j)

        scc = kosaraju(graph, n)
        if len(scc) == 1:
            print(1)
        else:
            print(0)
