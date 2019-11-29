"""
固定和的元素对

Description

输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。


Input

输入第一行为用例个数， 每个测试用例输入第一行是数组，每一个数用空格隔开；第二行是数字和。


Output

输出这样两个数有几对。


Sample Input 1

1
1 2 4 7 11 0 9 15
11
Sample Output 1

3
"""

import itertools


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        nums = list(map(int, input().split()))
        m = int(input())
        
        cnt = 0
        for a, b in itertools.combinations(nums, 2):
            if a + b == m:
                cnt += 1
        print(cnt)
        