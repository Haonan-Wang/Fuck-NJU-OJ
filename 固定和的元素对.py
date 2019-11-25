import itertools


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        nums = list(map(int, input().split()))
        m = int(input())
        
        cnt = 0
        for a, b in itertools.combinations(nums, 2):
            if a + b == m:
                cnt += 1
        print(cnt)
        