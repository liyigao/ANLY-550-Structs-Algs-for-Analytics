import time

def fib_iterative():
    timer = time.clock()
    fiblist = list()
    fiblist.append(0)
    fiblist.append(1)
    n = 1
    while (time.clock() - timer) < 60:
        fiblist.append((fiblist[n] + fiblist[n-1])%65536)
        n = n + 1
    return n, fiblist[n]

def main():
    print(fib_iterative())
    
main()
