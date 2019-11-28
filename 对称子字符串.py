"""
对称子字符串
Description

Given a string ‘str’ of digits, find length of the longest substring of ‘str’, such that the length of the substring is
2k digits and sum of left k digits is equal to the sum of right k digits.

给定字符串“ str”的数字，请找到最长字符串“ str”的长度，以使子字符串的长度为2k位，左k位的总和等于右k位的总和。
Input

输入第一行是测试用例的个数，后面每一行表示一个数字组成的字符串，例如："123123"


Output

输出找到的满足要求的最长子串的长度。例如，给定的例子长度应该是 6。每行对应一个用例的结果。


Sample Input 1

1
1538023
Sample Output 1

4
"""

def findMaxLen(nums):
    for k in range(len(nums) // 2, 0, -1):
        for mid in range(k, len(nums) - k + 1):
            if sum(nums[mid - k:mid]) == sum(nums[mid:mid + k]):
                return 2 * k
    return 0


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        nums = list(map(int, input()))
        print(findMaxLen(nums))
