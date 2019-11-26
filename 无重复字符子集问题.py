n = 0
nums = []
d = {}


def dp(status, cur):
    if cur >= n:
        return 0

    if (status, cur) in d:
        return d[(status, cur)]

    max_sum = dp(status, cur + 1)

    exist = False
    next_status = status
    for digit in str(nums[cur]):
        if status[int(digit)] == '1':
            exist = True
            break
        next_status = next_status[:int(digit)] + '1' + next_status[int(digit) + 1:]

    if not exist:
        max_sum = max([nums[cur] + dp(next_status, cur + 1), max_sum])

    d[(status, cur)] = max_sum
    return max_sum


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        d = {}
        print(dp('0' * 10, 0))
