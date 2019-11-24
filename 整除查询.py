if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        input()
        nums = list(map(int, input().split()))
        query = list(map(int, input().split()))

        cnts = []
        for k in query:
            cnt = 0
            for num in nums:
                if num % k == 0:
                    cnt += 1
            cnts.append(cnt)

        print(' '.join(map(str, cnts)))
