def merge_sort(arr):
    if len(arr) < 2:
        return 0, arr
    count = 0
    mid = len(arr) // 2
    c_left, left = merge_sort(arr[:mid])
    c_right, right = merge_sort(arr[mid:])
    for i in range(len(arr)):
        if not right or left and left[0] < right[0]:
            arr[i] = left.pop(0)
        else:
            arr[i] = right.pop(0)
            count += len(left)
    return count + c_left + c_right, arr


def get_num(arr):
    return merge_sort(arr)[0]


case = int(input().strip())
while case:
    size = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(get_num(arr))
    case -= 1
