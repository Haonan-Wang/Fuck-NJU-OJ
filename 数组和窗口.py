if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        w = int(input())

        begin, sum_max = 0, 0
        while begin + w <= len(nums):
            sum_max += max(nums[begin:begin + w])
            begin += 1
        print(sum_max)
