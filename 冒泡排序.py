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
