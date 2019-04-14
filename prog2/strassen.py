## Yigao Li, Tao Yu
## ANLY 550
## Programming Assignment 2

import math
import random
import sys
import time

## Pad 0s to odd dimension matrix
def pad0(matrix):
    n = len(matrix)
    output = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            output[i][j] = matrix[i][j]
    return output

## Matrix addition
def plus(a, b):
    n = len(a)
    output = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            output[i][j] = a[i][j] + b[i][j]
    return output

## Matrix subtraction
def minus(a, b):
    n = len(a)
    output = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            output[i][j] = a[i][j] - b[i][j]
    return output

## Conventional matrix multiplication algorithm
def convention(a, b):
    n = len(a)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

## Strassen's algorithm
def strassen(a, b):
    n = len(a)
    ## For some small n, use conventional algorithm
    convention_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,21,23,25,27,29,31,33,37]
    if n in convention_list:
        return convention(a,b)
    else:
        if n%2 == 1:
            a = pad0(a)
            b = pad0(b)
            n = n + 1
        div = int(n/2)
        x = [[0 for j in range(div)] for i in range(div)]
        y = [[0 for j in range(div)] for i in range(div)]
        z = [[0 for j in range(div)] for i in range(div)]
        w = [[0 for j in range(div)] for i in range(div)]
        e = [[0 for j in range(div)] for i in range(div)]
        f = [[0 for j in range(div)] for i in range(div)]
        g = [[0 for j in range(div)] for i in range(div)]
        h = [[0 for j in range(div)] for i in range(div)]
        for i in range(div):
            for j in range(div):
                x[i][j] = a[i][j]
                y[i][j] = a[i][j+div]
                z[i][j] = a[i+div][j]
                w[i][j] = a[i+div][j+div]
                e[i][j] = b[i][j]
                f[i][j] = b[i][j+div]
                g[i][j] = b[i+div][j]
                h[i][j] = b[i+div][j+div]
        temp1 = minus(f, h)
        temp2 = plus(x, y)
        temp3 = plus(z, w)
        temp4 = minus(g, e)
        temp5 = plus(x, w)
        temp6 = plus(e, h)
        temp7 = minus(y, w)
        temp8 = plus(g, h)
        temp9 = minus(x, z)
        temp10 = plus(e, f)
        p1 = strassen(x, temp1)
        p2 = strassen(temp2, h)
        p3 = strassen(temp3, e)
        p4 = strassen(w, temp4)
        p5 = strassen(temp5, temp6)
        p6 = strassen(temp7, temp8)
        p7 = strassen(temp9, temp10)
        c11 = plus(p5, p4)
        c11 = minus(c11, p2)
        c11 = plus(c11, p6)
        c12 = plus(p1, p2)
        c21 = plus(p3, p4)
        c22 = plus(p5, p1)
        c22 = minus(c22, p3)
        c22 = minus(c22, p7)
        c = [[0 for j in range(n)] for i in range(n)]
        for i in range(div):
            for j in range(div):
                c[i][j] = c11[i][j]
                c[i][j+div] = c12[i][j]
                c[i+div][j] = c21[i][j]
                c[i+div][j+div] = c22[i][j]
        return c

## Remove 0s if padded before
def remove0s(matrix, N):
    output = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
         for j in range(N):
             output[i][j] = matrix[i][j]
    return output

## Read inputfile to matrices A and B
def read(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    n = int(math.sqrt(len(lines)/2))
    A = [[0 for j in range(n)] for i in range(n)]
    B = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = int(lines[n*i+j])
            B[i][j] = int(lines[n**2+n*i+j])
    return A, B

if __name__ == "__main__":

    flag = int(sys.argv[1])
    dimension = int(sys.argv[2])
    inputfile = str(sys.argv[3])
##    flag = 0
##    dimension = 39
##    inputfile = "inputfile.txt"
    A, B = read(inputfile)
##    start_time = time.clock()
    multi = strassen(A, B)
    result = remove0s(multi, dimension)
##    print(result)
##    print(time.clock() - start_time)
##    sys.stdout.write("{}\n".format(time.clock() - start_time))
    for i in range(dimension):
        sys.stdout.write("{}\n".format(result[i][i]))
    
