if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        txt, pat = input().split(',')

        idc = []
        begin = 0
        while begin < len(txt):
            idx = txt.find(pat, begin)
            if idx == -1:
                break

            idc.append(idx)
            begin = idx + 1
        
        print(' '.join(map(str, idc)))
        