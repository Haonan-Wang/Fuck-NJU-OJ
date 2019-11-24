if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        m = int(input())

        cnt = 0
        for begin in range(len(nums)):
            for end in range(begin + 1, len(nums) + 1):
                max_num = max(nums[begin:end])
                min_num = min(nums[begin:end])
                if max_num - min_num > m:
                    cnt += 1
        print(cnt)
