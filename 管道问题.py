if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, p = map(int, input().split())
        houses = set(range(1, n + 1))
        nex = [[0, 0] for i in range(n + 1)]
        while p:
            a, b, d = map(int, input().split())
            p -= 1
            houses.remove(b)
            nex[a] = [b, d]

        print(len(houses))
        for a in sorted(houses):
            b, min_d = nex[a]
            while nex[b][0]:
                b, d = nex[b]
                min_d = min(d, min_d)
            print(' '.join(map(str, [a, b, min_d])))
