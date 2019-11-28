'''
Description

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

给定文本txt[0..n-1]和模式pat[0..m-1]，编写一个函数搜索（char pat[]，char txt[]），它将pat[]在txt[]中的所有出现都打印出来。你可以假设n>m。

Input

输入第一行是用例个数，后面一行表示一个用例；用例包括两部分，第一部分为给定文本，第二部分为搜索串，两部分使用","隔开。


Output

每一个用例输出一行，每行按照找到的位置先后顺序排列，使用空格隔开。
'''

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        txt, pat = input().split(',')

        idc = []
        begin = 0
        while begin < len(txt):
            idx = txt.find(pat, begin)
            if idx == -1:
                break

            idc.append(idx)
            begin = idx + 1
        
        print(' '.join(map(str, idc)))
        