'''
Description

Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2. Append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.

Input:A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = {2, 1, 8, 3}Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

Since 2 is present first in A2[], all occurrences of 2s should appear first in A[], then all occurrences 1s as 1 comes after 2 in A[]. Next all occurrences of 8 and then all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]

Constraints:1 ≤ T ≤ 501 ≤ M ≤ 501 ≤ N ≤ 10 & N ≤ M1 ≤ A1[i], A2[i] ≤ 1000

给定两个数组A1[]和A2[]，对A1进行排序，使元素之间的相对顺序与A2中的相对顺序相同。对于A2中不存在的元素。最后按顺序追加。还指出A2[]中的元素数小于或等于A1[]中的元素数，并且A2[]具有所有不同的元素。
输入：A1[]={2，1，2，5，7，1，9，3，6，8，8}A2[]={2，1，8，3}输出：A1[]={2，2，1，1，8，8，3，5，6，7，9}
因为2在A2[]中首先出现，所以2s的所有出现都应该首先出现在A[]中，然后1s作为1出现在A[]中的2之后。接下来是8的所有出现，然后是3的所有出现。最后，我们打印A2[]中不存在的所有A1[]元素
约束条件：1≤T≤501≤M≤501≤N≤10&amp;N≤M1≤A1[i]，A2[i]≤1000

Input

The first line of input contains an integer T denoting the number of test cases. The first line of each test case is M and N. M is the number of elements in A1 and N is the number of elements in A2.The second line of each test case contains M elements. The third line of each test case contains N elements.


Output

Print the sorted array according order defined by another array.

'''


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
