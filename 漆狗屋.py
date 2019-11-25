import math


nums = []
d = {}


def dp(k, n):
    if (k, n) in d:
        return d[(k, n)]

    cur_sum = 0

    if k == 1:
        cur_sum = sum(nums[n:])
        d[(k, n)] = cur_sum
        return cur_sum

    ans = math.inf
    for i in range(n, len(nums) + 1):
        if i != n:
            cur_sum += nums[i - 1]
        ans = min([max([cur_sum, dp(k - 1, i)]), ans])
    d[(k, n)] = ans
    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        k, n = map(int, input().split())
        nums = list(map(int, input().split()))

        d = {}
        dp(k, 0)
        print(d[(k, 0)])
