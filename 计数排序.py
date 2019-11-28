"""
计数排序
Description

实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。
"""
def count_sort(nums):
    num2counts = []
    for num in nums:
        count = 0
        for other_num in nums:
            if other_num < num:
                count += 1
        num2counts.append((num, count))
    num2counts.sort(key=lambda num2count: num2count[1])
    nums = [num2count[0] for num2count in num2counts]
    return nums


if __name__ == "__main__":
    while True:
        try:
            nums = list(map(int, input().split()))
        except EOFError:
            break
        
        if len(nums) > 1:
            nums.pop(0)

        nums = count_sort(nums)
        print(' '.join(map(str, nums)))
