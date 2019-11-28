"""
订单问题
Description

Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders. The amount of
tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped Ai rupees and if
 Ankit takes this order, the tip would be Bi rupees.In order to maximize the total tip value they decided to distribute
  the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot
  take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal
   to N, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount
   of total tip money after processing all the orders.
描述：

Rahul和Ankit是Royal Restaurant中仅有的两个服务员。 今天，这家餐厅收到了N份订单。 当小费由不同的服务员处理时，小费的数量可能会有所不同，
如果拉胡尔接受第i个订单，则小费为艾卢比，如果安奇接受这笔订单，则小费为双卢比。为了最大化小费的总价值，他们决定 在彼此之间分配订单。 一
份订单只能由一个人处理。 同样，由于时间限制，Rahul不能接受超过X的订单，Ankit不能接受超过Y的订单。 确保X + Y大于或等于N，这意味着所有订
单都可以由Rahul或Ankit处理。 处理所有订单后，找出小费总额的最大可能金额。

Input

• The first line contains one integer, number of test cases.

• The second line contains three integers N, X, Y.

• The third line contains N integers. The ith integer represents Ai.

• The fourth line contains N integers. The ith integer represents Bi.


Output

Print a single integer representing the maximum tip money they would receive.


Sample Input 1

1
5 3 3
1 2 3 4 5
5 4 3 2 1
Sample Output 1

21
"""


N, X, Y = 0, 0, 0
A, B = [], []

d = {}


def dp(cur, i, j):
    if cur == N:
        return 0
    if (cur, i, j) in d:
        return d[(cur, i, j)]

    max_tip = 0
    if i < X:
        max_tip = max([A[cur] + dp(cur + 1, i + 1, j), max_tip])
    if j < Y:
        max_tip = max([B[cur] + dp(cur + 1, i, j + 1), max_tip])

    d[(cur, i, j)] = max_tip
    return max_tip


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        N, X, Y = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        d = {}
        print(dp(0, 0, 0))
