if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        n1, n2 = map(int, input().split())

        nums1 = list(map(int, input().split()))
        nums2 = list(map(int, input().split()))

        num2cnt = {}
        for num in nums1:
            if num not in num2cnt:
                num2cnt[num] = 0
            num2cnt[num] += 1

        res = []
        for num in nums2:
            if num not in num2cnt:
                continue
            res.extend([str(num)] * num2cnt[num])
            del num2cnt[num]

        num_cnts = list(num2cnt.items())
        num_cnts.sort(key=lambda num_cnt: num_cnt[0])
        for num, cnt in num_cnts:
            res.extend([str(num)] * cnt)

        print(' '.join(res))
