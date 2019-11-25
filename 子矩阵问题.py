def cal_max_rect(heights):
    s = []
    max_rect = 0
    heights.append(-1)
    for i in range(len(heights)):
        while s and heights[i] <= heights[s[-1]]:
            top = s.pop(-1)
            if s:
                begin = s[-1]
            else:
                begin = -1
            width = i - begin - 1
            max_rect = max([max_rect, heights[top] * width])
        s.append(i)
    return max_rect


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        m, n = map(int, input().split())
        nums = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            row = list(map(int, input().split()))
            for j in range(n):
                nums[i][j] = row[j]

        ans = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max([cal_max_rect(heights), ans])
        print(ans)
