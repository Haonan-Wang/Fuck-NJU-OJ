class Solution:
    def __init__(self, node2edges, vis):
        self.node2edges = node2edges
        self.vis = vis
        self.max_dep = 0

    def dfs(self, node, dep):
        is_end = True
        for next_node in self.node2edges[node]:
            if self.vis[next_node]:
                continue

            is_end = False
            self.vis[next_node] = True
            self.dfs(next_node, dep + 1)
            self.vis[next_node] = False
        if is_end:
            self.max_dep = max([dep, self.max_dep])

    def solute(self, begin):
        self.dfs(begin, 0)
        return self.max_dep


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

        print(Solution(node2edges, vis).solute(begin))
