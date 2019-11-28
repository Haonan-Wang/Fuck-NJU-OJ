'''
Description

Cows in the FooLand city are interesting animals. One of their specialties is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of two years and proceeds to produce other calves (one female calf a year).

Now the farmer Harold wants to know how many animals would he have at the end of N years, if we assume that none of the calves die, given that initially, he has only one female calf?

explanation:At the end of 1 year, he will have only 1 cow, at the end of 2 years he will have 2 animals (one parent cow C1 and other baby calf B1 which is the offspring of cow C1).At the end of 3 years, he will have 3 animals (one parent cow C1 and 2 female calves B1 and B2, C1 is the parent of B1 and B2).At the end of 4 years, he will have 5 animals (one parent cow C1, 3 offsprings of C1 i.e. B1, B2, B3 and one offspring of B1).

傻瓜和城市里的牛是有趣的动物。他们的专长之一是生产后代。傻瓜的一头母牛，两岁时产下第一头小牛（母牛），然后继续生产其他小牛（每年产一头母牛）。
现在，农夫哈罗德想知道，如果我们假设没有一头小牛死亡，那么在N年结束时，他会有多少头动物，假设最初，他只有一头母牛？
说明：1年结束时，他只有1头母牛，2年结束时，他将有2头母牛（一头母牛C1，另一头小牛B1是母牛C1的后代），3年结束时，他将有3头母牛（一头母牛C1和两头母牛B1和B2，C1是母牛B1和B2的后代），4年结束时，他将有5头动物（一头母牛C1，3个C1的后代，即B1、B2、B3和一个B1的后代）。

Input

The first line contains a single integer T denoting the number of test cases. Each line of the test case contains a single integer N as described in the problem.


Output

For each test case print in new line the number of animals expected at the end of N years modulo 10^9 + 7.
'''


mod = 1000000007
d = {0: 0, 1: 1, 2: 1}


def fib(n):
    if n < 3:
        return d[n]

    if n in d:
        return d[n]

    if (n % 2 == 1):
        k = (n + 1) // 2
        x = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % mod
        if x < 0:
            x += mod
        d[n] = x

    else:
        k = n // 2
        x = (fib(k) * ((fib(k + 1) * 2) - fib(k))) % mod
        if x < 0:
            x += mod
        d[n] = x
    return d[n]


if __name__ == "__main__":
    case = int(input())
    while case:
        n = int(input())
        print(fib(n + 1))
        case -= 1
