def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib_recursive(n-1) + fib_recursive(n-2))%65536

import time

def main():
    
    timer = time.clock()
    b = fib_recursive(1)
    a = fib_recursive(0)
    fib = a + b
    n = 1
    while (time.clock() - timer) < 60:
        b = fib
        a = fib_recursive(n)
        fib = (a + b)%65536
        n = n + 1
    print(n)
    print(fib)
    
main()
