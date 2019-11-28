def precompute(arr, diff):
    for i, pair in enumerate(arr):
        if i == 0:
            diff.append(pair[0] - 1)
        else:
            diff.append(diff[i - 1] + pair[0] - arr[i - 1][1] - 1)


def search_marks(arr, diff, rank):
    n = len(arr) - 1
    l = 0
    while l <= n:
        mid = (l + n) // 2
        if rank + diff[mid] >= arr[mid][0] and rank + diff[mid] <= arr[mid][1]:
            break
        elif rank + diff[mid] < arr[mid][0]:
            n = mid - 1
        else:
            l = mid + 1
    return rank + diff[mid]


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, q = map(int, input().split())
        arr, diff = [], []

        nums = list(map(int, input().split()))
        for i in range(n):
            arr.append((nums[i * 2], nums[i * 2 + 1]))
        precompute(arr, diff)

        ans = []
        for rank in map(int, input().split()):
            marks = search_marks(arr, diff, rank)
            ans.append(str(marks))
        print(' '.join(ans))
