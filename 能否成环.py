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
