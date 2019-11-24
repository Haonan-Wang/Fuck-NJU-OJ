if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        items = input().split()
        items.pop(0)
        k = int(items.pop(-1))

        for begin in range(0, len(items) - k + 1, k):
            items[begin:begin + k] = items[begin:begin + k][::-1]
        print(' '.join(items))
