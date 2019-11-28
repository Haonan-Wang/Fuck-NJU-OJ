"""
漆狗屋
Description

Dilpreet wants to paint his dog- Buzo's home that has n boards with different lengths[A1, A2,..., An]. He hired k
painters for this work and each painter takes 1 unit time to paint 1 unit of the board.The problem is to find the
minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards,
say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.

Constraints:1<=T<=100,1<=k<=30,1<=n<=50,1<=A[i]<=500

迪普雷特（Dilpreet）想要画他的狗-布佐（Buzo）的房屋，里面有n块不同长度的木板[A1，A2，...，An]。 他聘请了k名画家来完成这项工作，
每个画家要花1个单位的时间来涂漆1个单位的板子。问题是找到在任何画家只能涂漆连续部分的约束下完成这项工作的最短时间。
登上{2，3，4}或仅登上{1}或什么都没有登上{2，4，5}。

约束：1 <= T <= 100,1 <= k <= 30,1 <= n <= 50,1 <= A [i] <= 500

Input

The first line consists of a single integer T, the number of test cases. For each test case, the first line contains an
integer k denoting the number of painters and integer n denoting the number of boards. Next line contains n- space
separated integers denoting the size of boards.


Output

For each test case, the output is an integer displaying the minimum time for painting that house.


Sample Input 1

2
2 4
10 10 10 10
2 4
10 20 30 40
Sample Output 1

20
60
"""


import math


nums = []
d = {}


def dp(k, n):
    if (k, n) in d:
        return d[(k, n)]

    cur_sum = 0

    if k == 1:
        cur_sum = sum(nums[n:])
        d[(k, n)] = cur_sum
        return cur_sum

    ans = math.inf
    for i in range(n, len(nums) + 1):
        if i != n:
            cur_sum += nums[i - 1]
        ans = min([max([cur_sum, dp(k - 1, i)]), ans])
    d[(k, n)] = ans
    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        k, n = map(int, input().split())
        nums = list(map(int, input().split()))

        d = {}
        dp(k, 0)
        print(d[(k, 0)])
