def findMaxLen(nums):
    for k in range(len(nums) // 2, 0, -1):
        for mid in range(k, len(nums) - k + 1):
            if sum(nums[mid - k:mid]) == sum(nums[mid:mid + k]):
                return 2 * k
    return 0


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        nums = list(map(int, input()))
        print(findMaxLen(nums))
