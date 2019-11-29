"""
调整数组使差最小

Description

有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序； 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。


Input

输入第一行为用例个数， 每个测试用例输入为两行，分别为两个数组，每个值用空格隔开。


Output

输出变化之后的两个数组内元素和的差绝对值。


Sample Input 1

1
100 99 98 1 2 3
1 2 3 4 5 40
Sample Output 1

48
"""

import itertools
import sys

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.extend(B)
        s = len(A)
        h = int(s / 2)
        sum1 = 0
        qs = list(itertools.combinations(A, h))
        for h in range(len(A)):
            sum1 += int(A[h])
        st = len(qs)
        D = []
        ans = 999999999
        for i in range(st):
            D.extend(qs[i])
            sum = 0
            for j in range(len(D)):
                sum += int(D[j])
            gd = sum1 - sum
            sg = abs(sum - gd)
            if(ans > sg):
                ans = sg
            D = []
        print(ans)
