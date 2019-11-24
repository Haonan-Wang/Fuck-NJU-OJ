def topo(edges):
    if not edges:
        return 1

    nodes, in_nodes = set(), set()
    for edge in edges:
        nodes.update(edge)
        in_nodes.add(edge[1])

    start_nodes = nodes - in_nodes
    cnt = 0
    for node in start_nodes:
        next_edges = []
        for edge in edges:
            if edge[0] != node:
                next_edges.append(edge)
        cnt += topo(next_edges)
    return cnt


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        edges = [edge.split() for edge in input().split(',')]
        print(topo(edges))
