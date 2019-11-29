"""
矩阵计算

Description

让我们定义一个其重复公式如下的系列：

C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)
C(0)= 2
C(1)= 0
C(2)= 1
C(3)= 7

现在基于该系列，将形成大小为nn的矩阵Mi，j。左上角的单元格是（1,1），右下角的单元格是（n，n）。 矩阵的每个像元（i，j）包含1或0.如果C（（i * j）^ 3）为奇数，则Mi，j为1，否则为0.计算矩阵中的总数 。


Input

输入的第一行将包含一个整数'T'-测试用例的数量。 接下来的“ T”行中的每行均由整数n组成，表示矩阵的大小。


Output

对于每个测试用例，输出一个整数-大小为n * n的盘子的味道值。


Sample Input 1

1
2
Sample Output 1

0
"""

if __name__ == '__main__':
      C_arr = [0, 0, 1, 1, 1, 0, 1]
      for _ in range(int(input())):
          tar = int(input().strip())
          count = 0
          for i in range(1, tar + 1):
              for j in range(1, tar + 1):
                  if C_arr[(i % 7 * j % 7) ** 3 % 7] == 1:  # 这样求余防止溢出,
                      count += 1
          print(count)
