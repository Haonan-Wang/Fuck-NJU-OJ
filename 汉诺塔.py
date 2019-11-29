"""
汉诺塔

Description

汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。


Input

输入第一行为用例个数， 每个测试用例输入的第一行为N。


Output

移动步数。


Sample Input 1

1
2
Sample Output 1

8
"""

def func(n, fro, buf, to):
    if (n == 1):
        return 2

    step = 0
    step += func(n - 1, fro, buf, to)
    step += 1
    step += func(n - 1, to, buf, fro)
    step += 1
    step += func(n - 1, fro, buf, to)
    return step


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        print(func(n, 'a', 'b', 'c'))
        