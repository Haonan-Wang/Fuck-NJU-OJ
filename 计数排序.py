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
        nums.pop(0)

        nums = count_sort(nums)
        print(' '.join(map(str, nums)))
