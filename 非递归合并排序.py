"""
非递归合并排序
Description

合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。
"""
def merge(nums, begin, mid, end):
    left_cur, right_cur = begin, mid + 1
    merged_nums = []
    while left_cur <= mid and right_cur <= end:
        if nums[left_cur] < nums[right_cur]:
            merged_nums.append(nums[left_cur])
            left_cur += 1
        else:
            merged_nums.append(nums[right_cur])
            right_cur += 1
    if left_cur <= mid:
        merged_nums.extend(nums[left_cur:mid + 1])
    else:
        merged_nums.extend(nums[right_cur:end + 1])
    nums[begin:end + 1] = merged_nums


# def merge_sort(nums, begin, end):
#     if begin < end:
#         mid = (begin + end) // 2
#         merge_sort(nums, begin, mid)
#         merge_sort(nums, mid + 1, end)
#         merge(nums, begin, mid, end)


def merge_sort(nums):
    size = 1
    while size < len(nums):
        i = 0
        while i < len(nums):
            begin = i
            mid = begin + size - 1
            end = mid + size
            if end < len(nums):
                merge(nums, begin, mid, end)
            else:
                end = len(nums) - 1
                if mid < end:
                    merge(nums, begin, mid, end)
            i = end + 1
        size *= 2


if __name__ == "__main__":
    while True:
        try:
            nums = list(map(int, input().split()))[1:]
        except EOFError:
            break
        # merge_sort(nums, 0, len(nums) - 1)
        merge_sort(nums)
        print(' '.join(map(str, nums)))
