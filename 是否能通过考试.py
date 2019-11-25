if __name__ == '__main__':

    for _ in range(int(input())):
        n, h, p = list(map(int, input().strip().split()))  # 最大耗时就是最大容量
        h_arr = []  # 耗时  耗时作为重量
        p_arr = []  # 分数  分数作为价值
        for i in range(n):
            temp = list(map(int, input().strip().split()))
            h_arr.append(temp[0])
            p_arr.append(temp[-1])

        dp = [[0] * (h + 1) for _ in range((n + 1))]
        min_tar = h + 1
        for i in range(1, n + 1):
            for j in range(1, h + 1):
                if h_arr[i - 1] <= j:  # 如果可以放
                    op_add = dp[i - 1][j - h_arr[i - 1]] + p_arr[i - 1]  # 放入当前物品\
                    op_not = dp[i - 1][j]
                    dp[i][j] = max(op_add, op_not)
                else:  # 不能放
                    dp[i][j] = dp[i - 1][j]
                if dp[i][j] >= 21:  # 如果满足了条件,则记录当前时间
                    min_tar = min(min_tar, j)
        if dp[-1][-1] < p:
            print("NO")
        else:
            print("YES " + str(min_tar))
