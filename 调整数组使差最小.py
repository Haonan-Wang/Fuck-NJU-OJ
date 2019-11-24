import itertools
import sys

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.extend(B)
        s = len(A)
        h = int(s / 2)
        sum1 = 0
        qs = list(itertools.combinations(A, h))
        for h in range(len(A)):
            sum1 += int(A[h])
        st = len(qs)
        D = []
        ans = 999999999
        for i in range(st):
            D.extend(qs[i])
            sum = 0
            for j in range(len(D)):
                sum += int(D[j])
            gd = sum1 - sum
            sg = abs(sum - gd)
            if(ans > sg):
                ans = sg
            D = []
        print(ans)
