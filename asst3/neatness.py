def neatness(words, M):
    n = len(words)
    extras = [[None for i in range(n)] for j in range(n)]
    lc = [[0 for i in range(n)] for j in range(n)]
    c = [0 for i in range(n+1)]
    p = [0 for i in range(n)]
    l = []
##  Compute extra spaces
    for i in range(n):
        l.append(len(words[i]))
    for i in range(n):
        extras[i][i] = M - l[i]
        for j in range(i+1,n):
            extras[i][j] = extras[i][j-1] - l[j] - 1
##  Compute cube of extras for all lines
    for i in range(n):
        for j in range(i,n):
            if extras[i][j] < 0:
                lc[i][j] = float("Inf")
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = (extras[i][j])**3
##  Compute c, p
    for j in range(1,n+1):
        c[j] = float("Inf")
        for i in range(1,j+1):
            if c[i-1] + lc[i-1][j-1] < c[j]:
                c[j] = c[i-1] + lc[i-1][j-1]
                p[j-1] = i-1
    return c, p

def givelines(p, j, words):
    i = p[j-1]
    if i == 0:
        k = 0
    else:
        k = givelines(p, i-1, words) + 1
    print(words[i:j+1])
    return k

if __name__ == "__main__":
    with open("BuffyReview.txt", 'r') as f:
        review = f.read()
    words = review.split()
    M = 40
    print("M = 40")
    p,pos = neatness(words, M)
    del p[-1]
    del pos[-1]
    givelines(pos, len(words)-1, words)
    print("Penalty =", p[-1])
    M = 72
    print("M = 72")
    p,pos = neatness(words, M)
    del p[-1]
    del pos[-1]
    givelines(pos, len(words)-1, words)
    print("Penalty =", p[-1])
