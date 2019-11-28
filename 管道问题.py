"""
管道网络
Description

Every house in the colony has at most one pipe going into it and at most one pipe going out of it. Tanks and taps are
to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on
its roof and every house with only an incoming pipe and no outgoing pipe gets a tap. Find the efficient way for the
construction of the network of pipes.

殖民地中的每个房屋最多只能有一个管道进入，最多只能有一个管道离开。 储罐和水龙头的安装方式应是，每户只有一根出水管但没有进水管的房屋都在
其屋顶上安装了一个储水箱，而每户只有一根进水管而没有出水管的房屋都应安装水龙头。 寻找构建管网的有效方法。
Input

The first line contains an integer T denoting the number of test cases. For each test case, the first line contains two
integer n & p denoting the number of houses and number of pipes respectively. Next, p lines contain 3 integer inputs a,
b & d, d denoting the diameter of the pipe from the house a to house b.Constraints:1<=T<=50，1<=n<=20，1<=p<=50，1<=a,
 b<=20，1<=d<=100


Output

For each test case, the output is the number of pairs of tanks and taps installed i.e n followed by n lines that
 contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.


Sample Input 1

1
9 6
7 4 98
5 9 72
4 6 10
2 8 22
9 7 17
3 1 66
Sample Output 1

3
2 8 22
3 1 66
5 6 10
"""


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, p = map(int, input().split())
        houses = set(range(1, n + 1))
        nex = [[0, 0] for i in range(n + 1)]
        while p:
            a, b, d = map(int, input().split())
            p -= 1
            houses.remove(b)
            nex[a] = [b, d]

        print(len(houses))
        for a in sorted(houses):
            b, min_d = nex[a]
            while nex[b][0]:
                b, d = nex[b]
                min_d = min(d, min_d)
            print(' '.join(map(str, [a, b, min_d])))
