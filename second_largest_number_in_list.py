if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    Y = sorted(set(arr))
    print Y[-2]
