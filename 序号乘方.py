if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        p = int(input())
        i = 1
        while p >= i * i:
            p -= i * i
            i += 1
        print(i - 1)
