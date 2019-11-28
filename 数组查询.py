"""
数组查询
Description

Given an array, the task is to complete the function which finds the maximum sum subarray, where you may remove at most
one element to get the maximum sum.

给定一个数组，任务是完成查找最大和子数组的功能，您可以在其中最多删除一个元素以获得最大和。
Input

第一行为测试用例个数T；后面每两行表示一个用例，第一行为用例中数组长度N，第二行为数组具体内容。


Output

每一行表示对应用例的结果。


Sample Input 1

1
5
1 2 3 -4 5
Sample Output 1

11
Hint

例如，对一个数组A[] = {1, 2, 3, -4, 5}，要移除-4得到最大和的子数组，和为11.
"""


def maxSumSubarray(arr, n):
    fw = [arr[i] for i in range(n)]
    bw = [arr[i] for i in range(n)]
    for i in range(1, n):
        fw[i] = max(fw[i], fw[i] + fw[i - 1])
    for i in range(n - 2, -1, -1):
        bw[i] = max(bw[i], bw[i] + bw[i + 1])
    ans = arr[0]
    for i in range(n):
        if fw[i] == bw[i]:
            ans = max(ans, fw[i])
        else:
            ans = max(ans, fw[i] + bw[i] - (2 * arr[i]), fw[i] + bw[i] - arr[i])
    return ans


# 方法二
def maxSumSubarray_2(arr, n):
    # cur0表示未删时当前位置的最大值，cur1表示已删时当前位置的最大值
    cur0, cur1, ans, size = arr[0], 0, float("-inf"), len(arr)
    for i in range(1, size):
        cur1 = max(cur1 + arr[i], cur0)  # 前面位置已删，删当前位置值
        cur0 = max(arr[i], cur0 + arr[i])  # 上一个位置最大值为负值，上一个位置最大值为正值
        ans = max(ans, cur0, cur1)
    return ans if size > 1 else arr[0]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxSumSubarray_2(arr, n))
