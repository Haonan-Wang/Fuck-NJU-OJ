if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, begin = input().split()
        n = int(n)

        nodes = list(input().split())

        node2edges, vis = {}, {}
        for i in range(n):
            items = input().split()
            node = items[0]
            flags = list(map(int, items[1:]))

            edges = []
            for j in range(n):
                if flags[j] == 1:
                    edges.append(nodes[j])
            node2edges[node] = edges

            vis[node] = False

        path = []

        queue = [begin]
        vis[begin] = True
        while queue:
            head = queue.pop(0)
            path.append(head)
            for node in node2edges[head]:
                if vis[node]:
                    continue
                vis[node] = True
                queue.append(node)

        print(' '.join(path))
