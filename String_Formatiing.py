#!/usr/bin/python
def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))
		
if __name__ =  '__main__':
string , max_width = input(), int(input())
result = wrap(string , max_width)
print (result)