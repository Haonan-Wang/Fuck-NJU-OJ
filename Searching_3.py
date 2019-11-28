"""
Searching_3
Description

They declared Sonam as bewafa. Although she is not, believe me! She asked a number of queries to people regrading their
 position in a test. Now its your duty to remove her bewafa tag by answering simple queries. All the students who give
 test can score from 1 to 10^18. Lower the marks, better the rank. Now instead of directly telling the marks of student
 they have been assigned groups where marks are distributed in continuous intervals, you have been given l(i) lowest
 mark of interval i and r(i) highest marks in interval i. So marks distribution in that interval is
 given as l(i), l(i)+1, l(i)+2 . . . r(i)

Now Sonam ask queries in which she gives rank of the student (x) and you have to tell marks obtained by that student

Note: rank1 is better than rank2 and rank2 is better than rank3 and so on and the first interval starts from 1.

Constraints:1<=T<=50,1<=N<=10^5,1<=Q<=10^5,1<= l(i) < r(i) <=10^18,1<=x<=10^18
他们宣布索南为bewafa。 虽然她不是，但请相信我！ 她向人们提出了一些疑问，要求人们改变他们在测试中的位置。
现在，您有责任通过回答简单的查询来删除她的bewafa标签。 所有参加考试的学生都可以得分1到10 ^ 18。 降低分数，提高排名。 现在，
您没有直接告诉学生分数，而是给他们分配了按连续时间间隔分配分数的组，而是给了我i（i）最低的间隔i和r（i）最高的间隔i。
因此，该间隔内的标记分布为l（i），l（i）+ 1，l（i）+2。 。 。 （

现在，索南（Sonam）提出询问，询问她给学生的等级（x），您必须告诉该学生获得的分数

注意：等级1优于等级2，等级2优于等级3，依此类推，第一个间隔从1开始。

Input

The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. Each test case
contains two space separated values N and Q denoting the no of groups and number of queries asked respectively. The next
 line contains N group of two integers separated by space which shows lowest marks in group i ie l(i) and highest marks
  in group i ie r(i) such that if i < j then r(i) < l(j). The next lines contain Q space separated integers x, denoting
   rank of student.


Output

For each query output marks obtain by student whose rank is x(1<=x<=10^18).


Sample Input 1

1
3 3
1 10 12 20 22 30
5 15 25
Sample Output 1

5 16 27
"""


def precompute(arr, diff):
    for i, pair in enumerate(arr):
        if i == 0:
            diff.append(pair[0] - 1)
        else:
            diff.append(diff[i - 1] + pair[0] - arr[i - 1][1] - 1)


def search_marks(arr, diff, rank):
    n = len(arr) - 1
    l = 0
    while l <= n:
        mid = (l + n) // 2
        if rank + diff[mid] >= arr[mid][0] and rank + diff[mid] <= arr[mid][1]:
            break
        elif rank + diff[mid] < arr[mid][0]:
            n = mid - 1
        else:
            l = mid + 1
    return rank + diff[mid]


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        n, q = map(int, input().split())
        arr, diff = [], []

        nums = list(map(int, input().split()))
        for i in range(n):
            arr.append((nums[i * 2], nums[i * 2 + 1]))
        precompute(arr, diff)

        ans = []
        for rank in map(int, input().split()):
            marks = search_marks(arr, diff, rank)
            ans.append(str(marks))
        print(' '.join(ans))
