def maxSumSubarray(arr, n):
    fw = [arr[i] for i in range(n)]
    bw = [arr[i] for i in range(n)]
    for i in range(1, n):
        fw[i] = max(fw[i], fw[i] + fw[i - 1])
    for i in range(n - 2, -1, -1):
        bw[i] = max(bw[i], bw[i] + bw[i + 1])
    ans = arr[0]
    for i in range(n):
        if fw[i] == bw[i]:
            ans = max(ans, fw[i])
        else:
            ans = max(ans, fw[i] + bw[i] - (2 * arr[i]), fw[i] + bw[i] - arr[i])
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxSumSubarray(arr, n))
