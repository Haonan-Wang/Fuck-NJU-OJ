"""
Description

Given a square grid of size n, each cell of which contains integer cost which represents a cost to traverse through that cell,
we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.

Note : It is assumed that negative cost cycles do not exist in input matrix.


描述

给定一个大小为n的正方形网格，其中每个单元格都包含整数成本，代表通过该单元格所要经过的成本，我们需要找到一条从左上角单元格到右下角单元格的路径，由此产生的总成本最小。


Input

The first line of input will contain number of test cases T. Then T test cases follow . Each test case contains 2 lines.
The first line of each test case contains an integer n denoting the size of the grid.
Next line of each test contains a single line containing N*N space separated integers depecting cost of respective cell from (0,0) to (n,n).

Constraints:1<=T<=50，1<= n<= 50


Output

For each test case output a single integer depecting the minimum cost to reach the destination.


Sample Input 1 

2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14


Sample Output 1

327
63
"""


if __name__ == "__main__":
    pass
