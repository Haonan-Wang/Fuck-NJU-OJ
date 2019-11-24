if __name__ == "__main__":
    T = int(input())

    while T:
        T -= 1

        nums = list(map(int, input().split()))
        intervals = list(map(int, input().split()))

        for interval in intervals:
            for begin in range(interval):
                for p in range(begin, len(nums), interval):
                    min_idx = p
                    for q in range(p + interval, len(nums), interval):
                        if nums[q] < nums[min_idx]:
                            min_idx = q
                    nums[p], nums[min_idx] = nums[min_idx], nums[p]

        print(' '.join(map(str, nums)))
