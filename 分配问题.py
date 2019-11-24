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
