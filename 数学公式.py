"""
数学公式
Description

Implement pow(A, B) % C.In other words, given A, B and C, find (A^B)%C

实施pow（A，B）％C.换句话说，给定A，B和C，找到（A ^ B）％C
Input

The first line of input consists number of the test cases. The following T lines consist of 3 numbers each separated by
 a space and in the following order:A B C'A' being the base number, 'B' the exponent (power to the base number) and 'C'
 the modular.Constraints:1 ≤ T ≤ 70,1 ≤ A ≤ 10^5,1 ≤ B ≤ 10^5,1 ≤ C ≤ 10^5


Output

In each separate line print the modular exponent of the given numbers in the test case.


Sample Input 1

3
3 2 4
10 9 6
450 768 517
Sample Output 1

1
4
34
"""


def quick(a, b, c):
    ans = 1
    a = a % c
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        a, b, c = map(int, input().split())
        print(quick(a, b, c))
