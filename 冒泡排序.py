"""
冒泡排序
Description

实现冒泡排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。
"""
def my_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == "__main__":
    while True:
        try:
            nums = list(map(int, input().split()))
        except EOFError:
            break
        nums.pop(0)

        nums = my_sort(nums)
        print(' '.join(map(str, nums)))
