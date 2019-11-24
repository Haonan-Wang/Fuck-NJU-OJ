INITIAL_STR = '12345'


def findCh(length, i, pos):
    if i == 1:
        STR_1 = INITIAL_STR + '$' + INITIAL_STR[::-1]
        return STR_1[pos]

    mid_begin = (length - i) // 2
    mid_end = mid_begin + i - 1

    if pos < mid_begin:
        return findCh(mid_begin, i - 1, pos)
    elif pos > mid_end:
        return findCh(mid_begin, i - 1, pos - mid_end - 1)
    else:
        return '$'


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        pos = int(input())

        length = len(INITIAL_STR)
        i = 0
        while length < pos:
            i += 1
            length = 2 * length + i
        if i == 0:
            print(INITIAL_STR[pos - 1])
        else:
            print(findCh(length, i, pos - 1))
