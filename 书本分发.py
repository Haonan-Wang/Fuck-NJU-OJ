# 就按照顺序遍历数组累和,如果超过桶容量证明装不下了,桶数量+1,重新换一个新桶
def get_required_painters(arr, cap):
    sum = 0
    numPainters = 1
    for x in arr:
        sum += x
        if sum > cap:
            numPainters += 1
            sum = x
    return numPainters


# 二分查找
# 对桶容量进行二分查找,获取当前桶容量对应的桶的个数,根据桶的个数决定查找方向  {key:桶容量,value:桶的个数}
def search(i, j, arr, k):
    if i == j:
        print(i)
        return
    mid = (i + j) >> 1
    p_num = get_required_painters(arr, mid)  # 以mid为容量的桶,需要多少个才能把数全装完
    if p_num <= k:  # 如果当前的桶的个数比要找的桶的数量小,说明当前桶数量过少,容量过大,因此就向左搜索,
        #  等于也要搜索,因为在桶数量保持不变时,当前容量未必是最小容量
        search(i, mid, arr, k)
    else:
        search(mid + 1, j, arr, k)


if __name__ == '__main__':
    for _ in range(int(input())):
        _ = input()
        arr = list(map(int, input().strip().split(" ")))
        k = list(map(int, input().strip().split(" ")))[0]
        min_cap = max(arr)  # 40
        max_cap = sum(arr)  # 100
        if len(arr) < k:
            print(-1)
        else:
            search(min_cap, max_cap, arr, k)
