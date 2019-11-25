if __name__ == '__main__':
    for _ in range(int(input())):
        # init
        s = input()
        s_arr = sorted(list(set(map(lambda x: ord(x) - ord("A"), s))))
        arr = [0] * 26
        for x in s_arr:
            arr[x] = 1
        # core
        # print(arr)
        best_count = 0
        best_res = " "
        for i in range(len(arr)):  # 遍历数组,首先选定第i个数
            if arr[i] == 1:  # 若当前数存在
                k = 1  # 步长从1开始
                while i + k < len(arr):  # 指定步长为1,2,...k
                    count = 0
                    res = ""
                    for j in range(i, len(arr), k):  # 按照步长去遍历每个数
                        if arr[j] == 1:  # 若该数存在
                            count += 1
                            res = chr(j + ord("A")) + res
                        else:  # 该数不存在则停止
                            break
                    if count > best_count:
                        best_res = res
                        best_count = count
                    elif count == best_count:
                        if res[0] > best_res[0]:
                            best_res = res
                    k += 1
        print(best_res)
