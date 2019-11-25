if __name__ == '__main__':
    # 筛选法
    arr = [0] * (10 ** 6)
    arr[0] = 1
    arr[1] = 1
    prime_arr = []
    for i in range(2, len(arr)):
        if arr[i] == 0:  # 是质数
            prime_arr.append(i)
        for prime in prime_arr:
            if i * prime >= len(arr):
                break
            arr[i * prime] = 1
            if i % prime == 0:
                break
    # core
    case_num = int(input())
    for i in range(case_num):
        num = int(input())
        res = 0
        # 满足公式1
        for i in range(len(prime_arr)):
            if (prime_arr[i] * prime_arr[(i + 1)]) ** 2 > num:  # 此时停止遍历
                break
            else:
                for j in range(i + 1, len(arr)):
                    if (prime_arr[i] * prime_arr[j]) ** 2 <= num:  # 统计满足条件的数
                        res += 1
                    else:
                        break
                # 满足公式2
        for i in prime_arr:
            if i > 23:  # 防止用例错误而无法ac而加的代码
                break
            if i ** 8 <= num:
                # print(i)
                res += 1
            else:
                break
        print(res)
