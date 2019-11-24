def select_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = -1
        for j in range(i, len(nums)):
            if min_idx == -1 or nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        nums.pop(0)

        nums = select_sort(nums)
        print(' '.join(map(str, nums)))
