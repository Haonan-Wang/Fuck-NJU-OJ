"""
Description

Mike is a lawyer with the gift of photographic memory. He is so good with it that he can tell you all the numbers on a sheet of paper by having a look at it without any mistake.
Mike is also brilliant with subsets so he thought of giving a challange based on his skill and knowledge to Rachael. Mike knows how many subset are possible in an array of N integers.
The subsets may or may not have the different sum. The challenge is to find the maximum sum produced by any subset under the condition:

The elements present in the subset should not have any digit in common.

Note: Subset {12, 36, 45} does not have any digit in common and Subset {12, 22, 35} have digits in common.Rachael find it difficult to win the challenge and is asking your help.
Can youhelp her out in winning this challenge?


描述

迈克（Mike）是一位拥有摄影记忆的律师。 他非常擅长使用它，只要看一眼就能毫无误解地告诉您一张纸上的所有数字。 Mike在子集方面也很出色，因此他考虑根据自己的技能和知识向Rachael提出挑战。 Mike知道N个整数数组中可能有多少个子集。
子集可以具有或可以不具有不同的和。 挑战在于找到在以下条件下任何子集产生的最大和：子集中存在的元素不应有任何共同的数字。


Input

First Line of the input consist of an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of a numbe N denoting the length of the array.
Second line of each test case consist of N space separated integers denoting the array elements.

Constraints:

1 <= T <= 100

1 <= N <= 100

1 <= array elements <= 100000


Output

Corresponding to each test case, print output in the new line.


Sample Input 1 

1
3
12 22 35


Sample Output 1

57
"""


n = 0
nums = []
d = {}


def dp(status, cur):
    if cur >= n:
        return 0

    if (status, cur) in d:
        return d[(status, cur)]

    max_sum = dp(status, cur + 1)

    exist = False
    next_status = status
    for digit in str(nums[cur]):
        if status[int(digit)] == '1':
            exist = True
            break
        next_status = next_status[:int(digit)] + '1' + next_status[int(digit) + 1:]

    if not exist:
        max_sum = max([nums[cur] + dp(next_status, cur + 1), max_sum])

    d[(status, cur)] = max_sum
    return max_sum


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        d = {}
        print(dp('0' * 10, 0))
