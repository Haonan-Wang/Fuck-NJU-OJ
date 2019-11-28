"""
Description

Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.
Your are required to complete the function which returns an integer denoting the minimum number of swaps,
required to sort the array.


描述

给定一个由N个不同的elementsA []组成的数组，找到对数组进行排序所需的最小交换次数。您需要完成该函数，该函数返回一个表示对数组进行排序所需的最小交换次数的整数。


Input

The first line of input contains an integer T denoting the no of test cases . Then T test cases follow .
Each test case contains an integer N denoting the no of element of the array A[ ].
In the next line are N space separated values of the array A[ ] .(1<=T<=100;1<=N<=100;1<=A[] <=1000)


Output

For each test case in a new line output will be an integer denoting minimum umber of swaps that are required to sort the array.


Sample Input 1 

2
4
4 3 2 1
5
1 5 4 3 2


Sample Output 1

2
2
"""


def min_swaps(arr):
    n = len(arr)
    
    arrPos = [[num, i] for i, num in enumerate(arr)]
    arrPos.sort(key=lambda item: item[0])

    vis = [False] * n

    ans = 0
    for i in range(n):
        if vis[i] or arrPos[i][1] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = 1
            j = arrPos[j][1]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        N = int(input())
        arr = list(map(int, input().split()))
        
        print(min_swaps(arr))
