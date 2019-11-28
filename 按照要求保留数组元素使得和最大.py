"""
Description

Given an array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number Ai,
delete one occurrence of Ai-1 (if exists) and Ai each from the array. Repeat these steps until the array gets empty.
The problem is to maximize the sum of selected numbers.


描述

给定N个数字的数组，我们需要最大化所选数字的总和。 在每个步骤中，您需要选择一个数字Ai，从数组中删除一次出现的Ai-1（如果存在）和Ai。 重复这些步骤，直到数组变空。 问题是最大化所选数字的总和。


Input

The first line of the input contains T denoting the number of the test cases. For each test case,
the first line contains an integer n denoting the size of the array. Next line contains n space separated integers denoting the elements of the array.

Constraints:1<=T<=100，1<=n<=50，1<=A[i]<=20

Note: Numbers need to be selected from maximum to minimum.


Output

For each test case, the output is an integer displaying the maximum sum of selected numbers.


Sample Input 1 

2
3
1 2 3
6
1 2 2 2 3 4


Sample Output 1

4
10
"""


def res(arr, n):
    dp = [0] * 21
    for i in range(n):
        dp[arr[i]] += 1

    s = 0
    for i in range(20, -1, -1):
        if(dp[i] > 0):
            s += i * dp[i]
            dp[i - 1] -= dp[i]

    return s


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        print(res(nums, n))
