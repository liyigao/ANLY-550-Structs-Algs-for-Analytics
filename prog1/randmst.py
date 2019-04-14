## ANLY 550
## Spring 2018
## Programming Assignment 1
## Yigao Li, Tao Yu

import sys
import math
import random
import time
from heapq import heappop, heappush

def graph0d(numpoints):
    graph_matrix = []
    for i in range(numpoints):
        one_list=[]
        for j in range(numpoints):
            if i == j:
                one_list.append(0)
            elif i > j:
                one_list.append(graph_matrix[j][i])
            else:
                one_list.append(random.uniform(0,1))
        graph_matrix.append(one_list)
    return graph_matrix

def graphNd(numpoints, dimension):
    matrix = [[0 for a in range(numpoints)] for b in range(numpoints)]
    x = []
    y = []
    z = []
    v = []
    for i in range(numpoints):
        x.append(random.uniform(0,1))
        y.append(random.uniform(0,1))
        if dimension >= 3:
            z.append(random.uniform(0,1))
        else:
            z.append(0)
        if dimension == 4:
            v.append(random.uniform(0,1))
        else:
            v.append(0)
    for j in range(numpoints):
        for k in range(j,numpoints):
            if k == j:
                matrix[j][k] = 0
            else:
                matrix[j][k] = math.sqrt((x[j]-x[k])**2 + (y[j]-y[k])**2 + (z[j]-z[k])**2 + (v[j]-v[k])**2)
                matrix[k][j] = matrix[j][k]
    return matrix

def convert(matrix):
    outputdict = {}
    num = len(matrix)
    for i in range(num):
        pairs = []
        for j in range(num):
            if i != j:
                pairs.append([j, matrix[i][j]])
        outputdict[i] = pairs
    return outputdict

def convertlarge(matrix):
    outputdict = {}
    num = len(matrix)
    for i in range(num):
        pairs = []
        for j in range(num):
            if i != j and matrix[i][j] < 0.2:
                pairs.append([j, matrix[i][j]])
        outputdict[i] = pairs
    return outputdict

def prim(graph):
    output = 0
    visit = set()
    start = next(iter(graph))
    unused = [(0, start)]
    while unused:
        weight, smallest = heappop(unused)
        if smallest not in visit:
            visit.add(smallest)
            output += weight
            for neighbor, weight in graph[smallest]:
                if neighbor not in visit:
                    heappush(unused, (weight, neighbor))
    return output

if __name__ == "__main__":
    
    flag = int(sys.argv[1])
    numpoints = int(sys.argv[2])
    numtrials = int(sys.argv[3])
    dimension = int(sys.argv[4])

    #start_time = time.clock()
    total = 0
    for i in range(numtrials):
        if dimension == 0:
            graph_matrix = graph0d(numpoints)
        else:
            graph_matrix = graphNd(numpoints, dimension)
        #sys.stdout.write("graph complete\n")
        if numpoints > 4000:
            graph_dict = convertlarge(graph_matrix)
        else:
            graph_dict = convert(graph_matrix)
        weight = prim(graph_dict)
        total += weight
        #sys.stdout.write("time elapse:{}s\n".format(time.clock() - start_time))
    average = total/numtrials
    #sys.stdout.write("time elapse:{}s\n".format(time.clock() - start_time))
    #print(average)
    sys.stdout.write("{} {} {} {}".format(average, numpoints, numtrials, dimension))
