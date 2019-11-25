def min_swaps(arr):
    n = len(arr)
    
    arrPos = [[num, i] for i, num in enumerate(arr)]
    arrPos.sort(key=lambda item: item[0])

    vis = [False] * n

    ans = 0
    for i in range(n):
        if vis[i] or arrPos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = 1
            j = arrPos[j][1]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        N = int(input())
        arr = list(map(int, input().split()))
        
        print(min_swaps(arr))
