'''
Description

There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets on both 
roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which 
has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of 
the road). The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads).
you need to help Geek to collect the maximum number of balls.

有两条平行的道路，每条分别包含N个和M个桶。每个桶里可能有一些球。这两条路上的桶都是按照桶里的球数来分类的。极客从一条路的尽头开始，这条路的桶里有较少
的球（也就是说，如果桶是按递增的顺序排列的，那么极客将从路的左边开始）。极客只能在交叉点改变道路（也就是说，两条道路上的球数相同的桶）。现在你需要帮
助GEKE收集最多的球数。

Input

The first line of input contains T denoting the number of test cases. The first line of each test case contains two integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains N integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of balls in buckets on the second road.

Constraints:1<= T <= 1000，1<= N <= 10^3，1<= M <=10^3，0<= A[i],B[i]<=10^6


Output

For each test case output a single line containing the maximum possible balls that Geek can collect.
'''


def maxCnt(road1, road2):
    ans = 0
    common = set(road1) & set(road2)
    arr1 = []
    arr2 = []
    for num in sorted(common):
        idx1 = road1.index(num)
        idx2 = road2.index(num)
        arr1.append(sum(road1[:idx1+1]))
        arr2.append(sum(road2[:idx2+1]))
        road1 = road1[idx1+1:]
        road2 = road2[idx2+1:]
    ans = max(sum(road1), sum(road2))
    for val1,val2 in zip(arr1, arr2):
        ans+=max(val1, val2)
    return ans
T = int(input())
while T:
    T -= 1
    n, m = map(int, input().split())
    road1 = list(map(int, input().split()))
    road2 = list(map(int, input().split()))
    ans = maxCnt(road1, road2)
    print(ans)