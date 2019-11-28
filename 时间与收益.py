class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, s):

        # Make the parent of nodes in the path from
        # u --> parent[u] point to parent[u]
        if s == self.parent[s]:
            return s
        self.parent[s] = self.find(self.parent[s])
        return self.parent[s]

    # Make us as parent of v
    def merge(self, u, v):

        # Update the greatest available
        # free slot to u
        self.parent[v] = u


def findmaxdeadline(arr, n):
    """ 
    :param arr: Job array 
    :param n: length of array 
    :return: maximum deadline from the set of jobs 
    """
    ans = -1
    for i in range(n):
        ans = max(ans, arr[i]['deadline'])
    return ans


def printjobscheduling(arr, n):
    id2profit = {item['id']: item['profit'] for item in arr}

    # Sort jobs in descending order on
    # basis of their profit
    arr = sorted(arr, key=lambda item: item['profit'], reverse=True)

    """ 
	Find the maximum deadline among all jobs and 
	create a disjoint set data structure with 
	max_deadline disjoint sets initially 
	"""
    max_deadline = findmaxdeadline(arr, n)
    ds = DisjointSet(max_deadline)

    cnt, sum_propfit = 0, 0
    for i in range(n):

        # find maximum available free slot for
        # this job (corresponding to its deadline)
        available_slot = ds.find(arr[i]['deadline'])
        if available_slot > 0:

            # This slot is taken by this job 'i'
            # so we need to update the greatest free slot.
            # Note: In merge, we make first parameter
            # as parent of second parameter.
            # So future queries for available_slot will
            # return maximum available slot in set of
            # "available_slot - 1"
            ds.merge(ds.find(available_slot - 1),
                     available_slot)
            cnt += 1
            sum_propfit += id2profit[arr[i]['id']]
    print(cnt, sum_propfit)


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        items = list(map(int, input().split()))
        arr = [{'id': items[3 * i],
                'deadline': items[3 * i + 1],
                'profit':items[3 * i + 2]
                } for i in range(n)]

        printjobscheduling(arr, n)
