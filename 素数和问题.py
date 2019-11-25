# 埃式筛选法
def no_of_primes(n):
    no_list = [1] * (n + 1)
    no_list[0] = 0
    no_list[1] = 0
    for i in range(2, n + 1):
        if no_list[i] == 1:
            for j in range(2 * i, n + 1, i):
                no_list[j] = 0
    return no_list


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        n = int(input())
        no_list = no_of_primes(n)
        for i in range(0, n):
            if no_list[i] == 1 and no_list[n - i] == 1:
                print(i, (n - i))
                break
