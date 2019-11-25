import functools


def cmp(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        nums = list(map(int, input().split()))

        num2cnt = {}
        for num in nums:
            if num not in num2cnt:
                num2cnt[num] = 0
            num2cnt[num] += 1

        num_cnts = list(num2cnt.items())
        num_cnts.sort(key=functools.cmp_to_key(cmp))

        num_strs = []
        for num_cnt in num_cnts:
            num_strs.extend([str(num_cnt[0])] * num_cnt[1])
        print(' '.join(num_strs))
