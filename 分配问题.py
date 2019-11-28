"""
分配问题
Description

对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。


Input

输入：第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；用例的第二行为使用逗号隔开的人员完成任务的成本；每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。


Output

输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。结果按照人员分配的任务序号大小排，第一个人员的任务序号大的放在前面，如果相同则看第二个人员的任务，以此类推。
"""
import itertools


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        n = int(input())
        items = input().split(',')

        costs = {}
        for item in items:
            person, task, cost = map(int, item.split())
            costs[(person, task)] = cost

        tasks = range(1, n + 1)
        permutations = itertools.permutations(tasks)

        min_cost = 1e20
        ans = []
        for tasks in permutations:
            sum_costs = 0
            for person, task in enumerate(tasks):
                sum_costs += costs[(person + 1, task)]
            if sum_costs < min_cost:
                min_cost = sum_costs
                ans = [tasks]
            elif sum_costs == min_cost:
                ans.append(tasks)

        ans = [' '.join(map(str, tasks)) for tasks in ans]
        ans.sort(reverse=True)
        print(','.join(ans))
