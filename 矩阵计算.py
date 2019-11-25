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
