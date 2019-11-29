"""
数组和窗口

Description

给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，每次向右滑动一个位置，求出每一次滑动时窗口内最大元素的和。


Input

输入第一行为用例个数， 每个测试用例输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。


Output

输出每个测试用例结果。


Sample Input 1

1
4 3 5 4 3 3 6 7
3
Sample Output 1

32
"""

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        w = int(input())

        begin, sum_max = 0, 0
        while begin + w <= len(nums):
            sum_max += max(nums[begin:begin + w])
            begin += 1
        print(sum_max)
