'''
Description

Archana is very fond of strings. She likes to solve many questions related to strings. She comes across a problem which she is unable 
to solve. Help her to solve. The problem is as follows: Given is a string of length L. Her task is to find the longest string from the
 given string with characters arranged in descending order of their ASCII code and in arithmetic progression. She wants the common 
 difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value.

阿尔查娜非常喜欢弦。她喜欢解答许多与弦有关的问题。她遇到了一个她无法解决的问题。帮她解决。问题如下：给定的是一个长度为L的字符串，
她的任务是从给定的字符串中找出最长的字符串，其中的字符按其ASCII码的降序排列，并按算术级数排列。她希望公共差异应该尽可能小（至少1个），
字符串的字符应该是更高的ASCII值。

Input

The first line of input contains an integer T denoting the number of test cases. Each test contains a string s of lengthL.

1<= T <= 100

3<= L <=1000

A<=s[i]<=Z

The string contains minimum three different characters.


Output

For each test case print the longest string.Case 1:Two strings of maximum length are possible- “CBA” and “RPQ”. But he wants the string to be of higher ASCII value therefore, the output is “RPQ”.Case 2:The String of maximum length is “JGDA”.
'''


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
