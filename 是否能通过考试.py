"""
Description

小张想要通过明天的考试。他知道考题的分值分布，也知道考试中要拿到每一个题目需要耗费的时间。假设考试时长为h，共n个题目，需要拿到p分才能通过考试
现在已知每个考题的得分与耗时，请你判断小张能否通过合理安排时间，而通过考试，并给出通过考试的最短时间。


Input

输入第一行为测试用例个数.每一个用例有若干行，第一行为任务数量n、考试时常h、通过分数p，下面的n行是每一个题目的耗时和得分。所有数值用空格分开。


Output

对每一个用例输出一行，如果能够通过考试，则输出“YES”和消耗最短时间，用空格隔开。 否则，输出“NO”。


Sample Input 1 

1
5 40 21 
12 10 
16 10 
20 10 
24 10 
8 3 


Sample Output 1

YES 36
"""


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
