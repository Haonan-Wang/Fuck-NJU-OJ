'''
Description

Given n Magnets which are placed linearly, with each magnet to be considered as of point object. Each magnet suffers force from its left sided magnets such that they repel it to the right and vice versa. All forces are repulsive. The force being equal to the distance (1/d , d being the distance). Now given the positions of the magnets, the task to find all the points along the linear line where net force is ZERO.

Note: Distance have to be calculated with precision of 0.0000000000001.

Constraints:1<=T<=100,1<=N<=100,1<=M[]<=1000

给定n个直线放置的磁铁，每个磁铁被视为点对象。每一块磁铁都受到其左侧磁铁的力，使其向右排斥，反之亦然。所有的力量都是排斥的。力等于距离（1/d，d为距离）。现在考虑到磁铁的位置，任务是找到所有的点沿直线，其中净力为零。
注意：距离必须以0.0000000000001的精度计算。
约束条件：1<=T<=100,1<=N<=100,1<=M[]<=1000

Input

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The second line of each test case contains an integer N. Then in the next line are N space separated values of the array M[], denoting the positions of the magnet.


Output

For each test case in a new line print the space separated points having net force zero till precised two decimal places.




'''

def zeroPoint(arr, n):
    ans = []
    for i in range(n - 1):
        tmp = 0
        tmpL = arr[i]
        tmpR = arr[i + 1]
        while True:
            left, right = 0, 0
            tmp = (tmpL + tmpR) / 2
            for l in range(i + 1):
                left += 1.0 / (tmp - arr[l])
            for r in range(i + 1, n):
                right += 1.0 / (arr[r] - tmp)
            if left - right > 0.000000001:
                tmpL = tmp
            elif right - left > 0.000000001:
                tmpR = tmp
            else:
                break
        ans.append(tmp)
    ans = list(map(lambda x: round(x, 2), ans))
    ans = map(lambda x: '%.02f' % x, ans)
    return ans


T = int(input())
while T:
    T -= 1
    n = int(input())
    arr = list(map(float, input().split()))
    ans = zeroPoint(arr, n)
    print(' '.join(ans))
