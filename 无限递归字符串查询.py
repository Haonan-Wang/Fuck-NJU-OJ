"""
无限递归字符串查询
Description

Consider a string A = "12345". An infinite string s is built by performing infinite steps on A recursively. In i-th
step, A is concatenated with ‘$’ i times followed by reverse of A. A=A|$...$|reverse(A), where | denotes concatenation.

Constraints:1<=Q<=10^5, 1<=POS<=10^12

考虑字符串A =“ 12345”。 无限字符串s通过对A递归执行无限步骤来构建。 在第i步中，A与” $”串联，
后跟A的反向。A = A | $ ... $ | reverse（A），其中| 表示串联。

约束条件：1 <= Q <= 10 ^ 5，1 <= POS <= 10 ^ 12

Input

输入第一行为查询次数，后面为每次查询的具体字符位置。


Output

输出每一次查询位置上的字符。


Sample Input 1

2
3
10
Sample Output 1

3
2
"""

INITIAL_STR = '12345'


def findCh(length, i, pos):
    if i == 1:
        STR_1 = INITIAL_STR + '$' + INITIAL_STR[::-1]
        return STR_1[pos]

    mid_begin = (length - i) // 2
    mid_end = mid_begin + i - 1

    if pos < mid_begin:
        return findCh(mid_begin, i - 1, pos)
    elif pos > mid_end:
        return findCh(mid_begin, i - 1, pos - mid_end - 1)
    else:
        return '$'


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        pos = int(input())

        length = len(INITIAL_STR)
        i = 0
        while length < pos:
            i += 1
            length = 2 * length + i
        if i == 0:
            print(INITIAL_STR[pos - 1])
        else:
            print(findCh(length, i, pos - 1))
