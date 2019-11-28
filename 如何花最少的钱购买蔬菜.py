"""
Description

Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable sellers in a line.
Each vegetable seller sells all three vegetable items, but at different prices. Rahul, obsessed by his nature to spend optimally,
decided not to purchase same vegetable from adjacent shops. Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop.
Rahul wishes to spend minimum money buying vegetables using this strategy. Help Rahul determine the minimum money he will spend.


描述

拉胡尔想购买蔬菜，主要是茄子，胡萝卜和番茄。 一行中有N个不同的蔬菜销售商。 每个蔬菜销售商出售所有三种蔬菜，但价格不同。 拉胡尔（Rahul）痴迷于最佳消费，因此决定不从附近的商店购买相同的蔬菜。
此外，Rahul将从一家商店购买一种蔬菜（仅1公斤）。 拉胡尔希望使用这种策略花费最少的钱购买蔬菜。 帮助拉胡尔确定他将花费的最低费用。


Input

First line indicates number of test cases T. Each test case in its first line contains N denoting the number of vegetable sellers in Vegetable Market.
Then each of next N lines contains three space separated integers denoting cost of brinjal, carrot and tomato per kg with that particular vegetable seller.


Output

For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.

Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4


Sample Input 1 

1
3
1 50 50
50 50 50
1 50 50


Sample Output 1

52
"""


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
