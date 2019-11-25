# 广度优先遍历图
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        N, start = map(str, input().split())
        N = int(N)
        A = list(map(str, input().split()))
        num = []
        result = []
        visited = set()
        for j in range(N):
            a = (list(map(str, input().split())))
            del a[0]
            num.append(list(map(int, a)))
        result.append(start)
        visited.add((start))
        while result:
            s = A.index(result[0])
            print(result[0], end=' ')
            result.pop(0)
            for j in range(N):
                if num[s][j] == 1:
                    if A[j] not in visited:
                        result.append(A[j])
                        visited.add((A[j]))
                        num[j][s] = 0
