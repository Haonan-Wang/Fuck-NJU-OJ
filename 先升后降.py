"""
先升后降

Description

从一列不重复的数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。


Input

输入第一行为用例个数， 每个测试用例输入是一个数组，数值通过空格隔开。


Output

输出筛选之后的数组，用空格隔开。如果有多种结果，则一行一种结果， 单个输入的所有结果按从小到大排序，排序的key的优先级随index递增而递减 例如 3 4 7 6； 1 3 7 5； 1 2 7 6； 1 3 7 6 排序成 1 2 7 6；1 3 7 5；1 3 7 6； 3 4 7 6；


Sample Input 1

4
1 2 4 7 11 10 9 15 3 5 8 6
1 3 5 4 7 6 4 5 3
1 2 3
3 2 1
Sample Output 1

1 2 4 7 11 10 9 8 6
1 3 4 7 6 4 3
1 3 4 7 6 5 3
1 3 5 7 6 4 3
1 3 5 7 6 5 3
1 2 3
3 2 1
"""

LIS_set = set()


def getLISLen(nums):
    len_list = []
    for i in range(len(nums)):
        len_list.append(1)
        for j in range(i):
            if nums[j] < nums[i]:
                len_list[i] = max([len_list[j] + 1, len_list[i]])
    return len_list


def getLIS(nums, len_list, LIS_idx):
    if len(LIS_idx) == 0:
        num_idx_limit = len(nums)
        max_len = max(len_list)
    else:
        num_idx_limit = LIS_idx[-1]
        max_len = len_list[num_idx_limit] - 1

    if max_len == 0:
        LIS = [nums[idx] for idx in LIS_idx]
        LIS.reverse()
        LIS_set.add(tuple(LIS))
        return

    for i in range(num_idx_limit):
        if len_list[i] != max_len:
            continue
        if num_idx_limit == len(nums) or nums[num_idx_limit] > nums[i]:
            getLIS(nums, len_list, LIS_idx + [i])


if __name__ == "__main__":
    T = int(input())
    while T > 0:
        T -= 1
        nums = list(map(int, input().split()))

        max_len = 0
        max_len_lists = []
        for mid_idx in range(len(nums)):
            left_len_list = getLISLen(nums[:mid_idx + 1])

            right_nums = nums[mid_idx:]
            right_nums.reverse()
            right_len_list = getLISLen(right_nums)

            length = max(left_len_list) + max(right_len_list) - 1
            if length >= max_len:
                if length > max_len:
                    max_len = length
                    max_len_lists.clear()
                max_len_lists.append({
                    'mid_idx': mid_idx,
                    'left': left_len_list,
                    'right': right_len_list
                })

        ans = set()
        for len_list in max_len_lists:
            mid_idx = len_list['mid_idx']

            LIS_set.clear()
            getLIS(nums[:mid_idx + 1], len_list['left'], [])
            left_set = LIS_set.copy()

            LIS_set.clear()
            right_nums = nums[mid_idx:]
            right_nums.reverse()
            getLIS(right_nums, len_list['right'], [])
            right_set = LIS_set.copy()

            for left_LIS in left_set:
                left_nums = list(left_LIS)
                for right_LIS in right_set:
                    right_nums = list(right_LIS)
                    right_nums.reverse()
                    ans.add(' '.join(map(str, left_nums + right_nums[1:])))

        for item in sorted(ans):
            print(item)
