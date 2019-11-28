'''
Description

Given the list of coins of distinct denominations and total amount of money. Output the minimum number of coins required to make up that amount. Output -1 if that money cannot be made up using given coins. You may assume that there are infinite numbers of coins of each type.

给出了不同面额和总金额的硬币清单。输出构成该数量所需的最小硬币数。产出-1，如果这些钱不能用给定的硬币来弥补。你可以假设每种类型的硬币数量是无限的。

Input

The first line contains 'T' denoting the number of test cases. Then follows description of test cases. Each cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct coins and total amount of money respectively. The second line contains N space-separated integers A1, A2, ..., AN denoting the values of coins. 

Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000


Output

Print the minimum number of coins required to make up that amount or return -1 if it is impossible to make that amount using given coins.

'''



coins = []


def solve(amount):
    if amount == 0:
        return 0

    for coin in coins:
        if amount - coin >= 0:
            res = solve(amount - coin)
            if res != -1:
                return 1 + res

    return -1


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, amount = map(int, input().split())
        coins = list(map(int, input().split()))

        coins.sort(reverse=True)
        print(solve(amount))
