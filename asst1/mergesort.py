import sys

def merge(s, t):
    r = []
    if s == []:
        return t
    elif t == []:
        return s
    elif s[0] <= t[0]:
        u = s.pop(0)
    elif s[0] > t[0]:
        u = t.pop(0)
    r = merge(s, t)
    r.insert(0, u)
    return r

def mergesort(a):
    n = len(a)
    if n == 1:
        return a
    cut = int(n/2)
    a1 = mergesort(a[:cut])
    a2 = mergesort(a[cut:])
    return merge(a1, a2)

if __name__ == "__main__":
    print("Enter a list numbers separated by comma(,)(ex: 1,2,3):")
    user_input = sys.stdin.readline()
    a = eval("[" + user_input + "]")
    sorted_list = mergesort(a)
    print("Sorted list is (ascending order):", sorted_list)
