def quick(a, b, c):
    ans = 1
    a = a % c
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        a, b, c = map(int, input().split())
        print(quick(a, b, c))
