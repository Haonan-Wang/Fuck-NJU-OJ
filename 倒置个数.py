"""
倒置个数
Description

有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，即i<j但是A[i]>A[j]则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)


Input

输入有多行，第一行整数T表示为测试用例个数，后面是T个测试用例，每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。


Output

输出每一个用例的倒置个数，一行表示一个用例。
"""
def merge_sort(arr):
    if len(arr) < 2:
        return 0, arr
    count = 0
    mid = len(arr) // 2
    c_left, left = merge_sort(arr[:mid])
    c_right, right = merge_sort(arr[mid:])
    for i in range(len(arr)):
        if not right or left and left[0] < right[0]:
            arr[i] = left.pop(0)
        else:
            arr[i] = right.pop(0)
            count += len(left)
    return count + c_left + c_right, arr


def get_num(arr):
    return merge_sort(arr)[0]


case = int(input().strip())
while case:
    size = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(get_num(arr))
    case -= 1
