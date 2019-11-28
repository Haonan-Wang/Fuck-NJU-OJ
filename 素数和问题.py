"""
Description

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only first such pair.

NOTE: A solution will always exist, read Goldbach’s conjecture.Also, solve the problem in linear time complexity, i.e., O(n).


描述

给定一个偶数（大于2），返回两个素数，它们的总和等于给定数。 有几种可能的组合。 仅打印第一对。


Input

The first line contains T, the number of test cases. The following T lines consist of a number each, for which we'll find two prime numbers.Note: The number would always be an even number.


Output

For every test case print two prime numbers space separated, such that the smaller number appears first. Answer for each test case must be in a new line.


Sample Input 1 

5
74
1024
66 
8
9990


Sample Output 1

3 71
3 1021
5 61
3 5
17 9973
"""


# 埃式筛选法
def no_of_primes(n):
    no_list = [1] * (n + 1)
    no_list[0] = 0
    no_list[1] = 0
    for i in range(2, n + 1):
        if no_list[i] == 1:
            for j in range(2 * i, n + 1, i):
                no_list[j] = 0
    return no_list


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        n = int(input())
        no_list = no_of_primes(n)
        for i in range(0, n):
            if no_list[i] == 1 and no_list[n - i] == 1:
                print(i, (n - i))
                break
