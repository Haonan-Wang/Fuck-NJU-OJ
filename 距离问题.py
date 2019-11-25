"""
距离问题
Description

In a given cartesian plane, there are N points. We need to find the Number of Pairs of points(A,B) such that

Point A and Point B do not coincide.
Manhattan Distance and the Euclidean Distance between the points should be equal.
Note : Pair of 2 points(A,B) is considered same as Pair of 2 points(B,A).

Manhattan Distance = |x2-x1|+|y2-y1|

Euclidean Distance = ((x2-x1)^2 + (y2-y1)^2)^0.5 where points are (x1,y1) and (x2,y2).

Constraints:1<=T <= 50, 1<=N <= 2*10 ^ 5, 0<=(|Xi|, |Yi|) <= 10^9


Input

First Line Consist of T - number of test cases. For each Test case:First Line consist of N , Number of points. Next line
 contains N pairs contains two integers Xi and Yi，i.e, X coordinate and the Y coordinate of a Point


Output

Print the number of pairs as asked above.


Sample Input 1

1
2
1 1
7 5
Sample Output 1

0
"""
from collections import defaultdict

if __name__ == '__main__':
    case_num = int(input())
    for i in range(case_num):
        dict_x = defaultdict(int)  # 初始化一个默认值为0的map
        dict_y = defaultdict(int)
        dict_xy = defaultdict(int)
        point_num = int(input())
        for j in range(point_num):
            p = [int(x) for x in input().strip().split(" ")]
            dict_x[p[0]] += 1
            dict_y[p[1]] += 1
            dict_xy[tuple(p)] += 1
        x_pair_num = 0
        y_pair_num = 0
        xy_pair_num = 0
        for k, v in dict_x.items():
            x_pair_num += v * (v - 1) // 2
        for k, v in dict_y.items():
            y_pair_num += v * (v - 1) // 2
        for k, v in dict_xy.items():
            xy_pair_num += v * (v - 1) // 2
        print(x_pair_num + y_pair_num - xy_pair_num)
