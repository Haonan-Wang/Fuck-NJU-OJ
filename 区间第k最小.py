"""
区间第k最小

Description

找到给定数组的给定区间内的第K小的数值。


Input

输入第一行为用例个数， 每个测试用例输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。


Output

结果。


Sample Input 1

1
1 2 3 4 5 6 7
3 5
2
Sample Output 1

4
"""

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        nums = list(map(int, input().split()))
        begin, end = map(int, input().split())
        k = int(input())

        sub = sorted(nums[begin - 1:end])
        print(sub[k - 1])
