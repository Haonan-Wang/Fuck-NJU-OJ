if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        begin, end = map(int, input().split())
        k = int(input())

        sub = sorted(nums[begin - 1:end])
        print(sub[k - 1])
