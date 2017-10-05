    N = int(raw_input())

    mylist = []
    
    for i in range(0, N):
        tokens = raw_input().strip().split()

        if tokens[0] == 'insert':
            mylist.insert(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'print':
            print mylist
        elif tokens[0] == 'remove':
            mylist.remove(int(tokens[1]))
        elif tokens[0] == 'append':
            mylist.append(int(tokens[1]))
        elif tokens[0] == 'sort':
            mylist.sort()
        elif tokens[0] == 'pop':
            mylist.pop()
        elif tokens[0] == 'reverse':
            mylist.reverse()