def partition(nums, begin, end):
    pivot = nums[begin]
    while begin < end:
        while begin < end and nums[end] >= pivot:
            end -= 1
        nums[begin] = nums[end]
        while begin < end and nums[begin] <= pivot:
            begin += 1
        nums[end] = nums[begin]
    nums[begin] = pivot
    return begin


# def quick_sort(nums, begin, end):
#     if begin < end:
#         mid = partition(nums, begin, end)
#         quick_sort(nums, begin, mid - 1)
#         quick_sort(nums, mid + 1, end)


def quick_sort(nums):
    begin, end = 0, len(nums) - 1
    cursors = [begin, end]
    while len(cursors) > 0:
        end = cursors.pop(-1)
        begin = cursors.pop(-1)
        if begin < end:
            mid = partition(nums, begin, end)
            if begin < mid:
                cursors.append(begin)
                cursors.append(mid - 1)
            if mid < end:
                cursors.append(mid + 1)
                cursors.append(end)


if __name__ == "__main__":
    while True:
        try:
            nums = list(map(int, input().split()))[1:]
        except EOFError:
            break
        # quick_sort(nums, 0, len(nums) - 1)
        quick_sort(nums)
        print(' '.join(map(str, nums)))
