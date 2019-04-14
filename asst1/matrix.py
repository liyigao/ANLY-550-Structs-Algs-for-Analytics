import time

def matrix_multi(a,b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0])%65536,
             (a[0][0]*b[0][1] + a[0][1]*b[1][1])%65536],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0])%65536,
             (a[1][0]*b[0][1] + a[1][1]*b[1][1])%65536]]
def main():
    timer = time.clock()
    fibmatrix = [[0,1],[1,1]]
    n = 1
    while (time.clock() - timer) < 60:
        fibmatrix = matrix_multi(fibmatrix, fibmatrix)
        n = n + 1
    print(n)
    print(fibmatrix[1][1])

main()
