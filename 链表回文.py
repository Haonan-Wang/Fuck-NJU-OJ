if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        
        items = input().split()
        items.pop(0)

        string = ''.join(items)
        if string == string[::-1]:
            print('true')
        else:
            print('false')
