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
