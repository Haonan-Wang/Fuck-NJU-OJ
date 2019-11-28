"""
链表区间逆序
Description

将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入第一行为用例个数， 每个测试用例输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。


Output

输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。
"""
if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        items = input().split()
        items.pop(0)
        k = int(items.pop(-1))

        for begin in range(0, len(items) - k + 1, k):
            items[begin:begin + k] = items[begin:begin + k][::-1]
        print(' '.join(items))
