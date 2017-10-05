if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    '''print n
    print integer_list'''
    
    T = tuple(integer_list)
    '''print T'''
    print hash(T)