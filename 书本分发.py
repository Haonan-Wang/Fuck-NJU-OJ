'''
Description

You are given N number of books. Every ith book has Pi number of pages. You have 
to allocate books to M number of students. There can be many ways or permutations to 
do so. In each permutation one of the M students will be allocated the maximum number of pages. 
Out of all these permutations, the task is to find that particular permutation in which the maximum 
number of pages allocated to a student is minimum of those in all the other permutations, and print this minimum
 value. Each book will be allocated to exactly one student. Each student has to be allocated atleast one book.

你得到了N本书。每本书都有π页数。你必须把书分配给M个学生。可以有许多方法或排列来这样做。在每一个排列中，一个m的学生将被分配
最多的页数。在所有这些排列中，任务是找到特定排列，其中分配给学生的最大页数在所有其他排列中最小，并打印该最小值。每本书将只分
配给一个学生。每个学生必须至少分配一本书。

Input

The first line contains 'T' denoting the number of testcases. Then follows description of T testcases:Each case begins with a single positive integer N denoting the number of books.The second line contains N space separated positive integers denoting the pages of each book.And the third line contains another integer M, denoting the number of studentsConstraints:1<= T <=70，1<= N <=50，1<= A [ i ] <=250，1<= M <=50，Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding)


Output

For each test case, output a single line containing minimum number of pages each student has to read for corresponding test case.
'''


# 就按照顺序遍历数组累和,如果超过桶容量证明装不下了,桶数量+1,重新换一个新桶
def get_required_painters(arr, cap):
    sum = 0
    numPainters = 1
    for x in arr:
        sum += x
        if sum > cap:
            numPainters += 1
            sum = x
    return numPainters


# 二分查找
# 对桶容量进行二分查找,获取当前桶容量对应的桶的个数,根据桶的个数决定查找方向  {key:桶容量,value:桶的个数}
def search(i, j, arr, k):
    if i == j:
        print(i)
        return
    mid = (i + j) >> 1
    p_num = get_required_painters(arr, mid)  # 以mid为容量的桶,需要多少个才能把数全装完
    if p_num <= k:  # 如果当前的桶的个数比要找的桶的数量小,说明当前桶数量过少,容量过大,因此就向左搜索,
        #  等于也要搜索,因为在桶数量保持不变时,当前容量未必是最小容量
        search(i, mid, arr, k)
    else:
        search(mid + 1, j, arr, k)


if __name__ == '__main__':
    for _ in range(int(input())):
        _ = input()
        arr = list(map(int, input().strip().split(" ")))
        k = list(map(int, input().strip().split(" ")))[0]
        min_cap = max(arr)  # 40
        max_cap = sum(arr)  # 100
        if len(arr) < k:
            print(-1)
        else:
            search(min_cap, max_cap, arr, k)
