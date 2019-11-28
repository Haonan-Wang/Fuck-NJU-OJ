"""
链表回文
Description

判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入第一行为用例个数， 每个测试用例输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值


Output

是回文则输出true，不是则输出false，一行表示一个链表的结果。
"""
if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        items = input().split()
        items.pop(0)

        string = ''.join(items)
        if string == string[::-1]:
            print('true')
        else:
            print('false')
