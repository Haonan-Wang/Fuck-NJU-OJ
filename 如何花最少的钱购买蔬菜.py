if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        a = []
        for i in range(n):
            tmp = list(map(int, input().split()))
            a.append(tmp)
        dp = [[0 for i in range(3)]for j in range(n)]
        dp[0][0] = a[0][0]
        dp[0][1] = a[0][1]
        dp[0][2] = a[0][2]
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + a[i][j]
        ans = 10**9
        for i in range(3):
            ans = min(ans, dp[n - 1][i])
        print(ans)
        t -= 1
