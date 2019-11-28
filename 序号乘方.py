"""
序号乘方
Description

There are Infinite People Standing in a row, indexed from 1.A person having index 'i' has strength of (i*i).You have
Strength 'P'. You need to tell what is the maximum number of People You can Kill With your Strength P.You can only
Kill a person with strength 'X' if P >= 'X' and after killing him, Your Strength decreases by 'X'.

有连续的无数人从1开始索引。索引为``i''的人的强度为（i * i），而强度为``P''的人。 您需要告诉您可以使用力量P杀死的最大人数是多少。
如果P> ='X'，您只能杀死具有力量'X'的人，杀死他之后，您的力量会降低'X'。
Input

First line contains an integer 'T' - the number of testcases,Each of the next 'T' lines contains an integer 'P'- Your Power.Constraints:1<=T<=100001<=P<=1000000000000000


Output

For each testcase Output The maximum Number of People You can kill.


Sample Input 1

1
14
Sample Output 1

3
"""

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        p = int(input())
        i = 1
        while p >= i * i:
            p -= i * i
            i += 1
        print(i - 1)
