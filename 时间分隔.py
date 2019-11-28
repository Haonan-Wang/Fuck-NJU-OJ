if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        arr = sorted(list(map(int, input().split())))
        dep = sorted(list(map(int, input().split())))

        cnt, ans = 1, 1
        i, j = 1, 0
        while i < n and j < n:
            if arr[i] < dep[j]:
                cnt += 1
                i += 1
                ans = max(cnt, ans)
            else:
                cnt -= 1
                j += 1
        print(ans)
