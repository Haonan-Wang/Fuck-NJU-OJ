"""
子数组的取值范围

Description

给定数组arr和整数num，求arr的连续子数组中满足：其最大值减去最小值的结果大于num的个数。请实现一个时间复杂度为O(length(arr))的算法。


Input

输入第一行为测试用例个数。每一个用例有若干行，第一行为数组，每一个数用空格隔开，第二行为num。


Output

输出一个值。


Sample Input 1

1
3 6 4 3 2
2
Sample Output 1

6
"""

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        m = int(input())

        cnt = 0
        for begin in range(len(nums)):
            for end in range(begin + 1, len(nums) + 1):
                max_num = max(nums[begin:end])
                min_num = min(nums[begin:end])
                if max_num - min_num > m:
                    cnt += 1
        print(cnt)
