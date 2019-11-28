'''Description

Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits. 

Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a train.

给定到达火车站的所有列车的到达和离开时间。你的任务是找到火车站所需的最少站台数，这样火车就不会等了。
注：考虑所有列车在同一天到达，在同一天离开。同样，火车的到达和离开时间也不能相同。

Input

The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively. 

Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.

Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359


Output

For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.
'''


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n = int(input())
        arr = sorted(list(map(int, input().split())))
        dep = sorted(list(map(int, input().split())))

        cnt, ans = 1, 1
        i, j = 1, 0
        while i < n and j < n:
            if arr[i] < dep[j]:
                cnt += 1
                i += 1
                ans = max(cnt, ans)
            else:
                cnt -= 1
                j += 1
        print(ans)
