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


# 方法二
def maxSumSubarray_2(arr, n):
    # cur0表示未删时当前位置的最大值，cur1表示已删时当前位置的最大值
    cur0, cur1, ans, size = arr[0], 0, float("-inf"), len(arr)
    for i in range(1, size):
        cur1 = max(cur1 + arr[i], cur0)  # 前面位置已删，删当前位置值
        cur0 = max(arr[i], cur0 + arr[i])  # 上一个位置最大值为负值，上一个位置最大值为正值
        ans = max(ans, cur0, cur1)
    return ans if size > 1 else arr[0]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxSumSubarray_2(arr, n))
