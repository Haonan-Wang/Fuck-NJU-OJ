def res(arr, n):
    dp = [0] * 21
    for i in range(n):
        dp[arr[i]] += 1

    s = 0
    for i in range(20, -1, -1):
        if(dp[i] > 0):
            s += i * dp[i]
            dp[i - 1] -= dp[i]

    return s


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        print(res(nums, n))
