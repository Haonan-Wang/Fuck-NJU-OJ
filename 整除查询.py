"""
整除查询
Description

Given an array of positive integers and many queries for divisibility. In every query Q[i], we are given an integer K ,
 we need to count all elements in the array which are perfectly divisible by K.
给定正整数数组和许多除数查询。 在每个查询Q [i]中，我们都得到一个整数K，我们需要计算数组中所有可以被K完全整除的元素。
Constraints:1<=T<=1001<=N,M<=1051<=A[i],Q[i]<=105


Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case consists of three lines. First line of each test case contains two integers N & M, second line contains N space
separated array elements and third line contains M space separated queries.


Output

For each test case,In new line print the required count for each query Q[i].


Sample Input 1

2
6 3
2 4 9 15 21 20
2 3 5
3 2
3 4 6
2 3
Sample Output 1

3 3 2
2 2
"""


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        input()
        nums = list(map(int, input().split()))
        query = list(map(int, input().split()))

        cnts = []
        for k in query:
            cnt = 0
            for num in nums:
                if num % k == 0:
                    cnt += 1
            cnts.append(cnt)

        print(' '.join(map(str, cnts)))
