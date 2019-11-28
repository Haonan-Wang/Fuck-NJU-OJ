"""
Description

Babul’s favourite number is 17. He likes the numbers which are divisible by 17.
This time what he does is that he takes a number N and tries to find the largest number which is divisible by 17,
by rearranging the digits. As the number increases he gets puzzled with his own task.
So you as a programmer have to help him to accomplish his task.Note:
If the number is not divisible by rearranging the digits, then print “Not Possible”. N may have leading zeros.


描述

Babul最喜欢的数字是17。他喜欢可以被17整除的数字。这次，他所做的是他将数字N取整，并尝试通过重新排列数字找到最大的可以被17整除的数字。
随着人数的增加，他对自己的任务感到困惑。 因此，作为程序员，您必须帮助他完成任务。注：如果无法通过重新排列数字来将数字整除，请打印“不可能”。
N可能有前导零。


Input

The first line of input contains an integer T denoting the no of test cases. Each of the next T lines contains the number N.


Output

For each test case in a new line print the desired output.


Sample Input 1 

4
17
43
15
16


Sample Output 1

17
34
51
Not Possible
"""


from itertools import permutations

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        array = list(map(lambda x: x, s))  # 把输入字符转成一个字符数组
        pailie = list(set(permutations(array)))  # 将数字全排列并去重
        max_z = 0
        for x in pailie:
            z = int("".join(x))  # 字符数组拼接成一个字符串,并转为数字
            if z % 17 == 0:
                max_z = max(max_z, z)  # 由于一个全排列可能有多个满足条件的数,因此选择一个最大的
        if max_z == 0:  # 注意,这里0一定要排除掉
            print("Not Possible")
        else:
            print(max_z)
