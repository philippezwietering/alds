def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

def badqsort(a,low=None,high=None):
    if high == None:
        high = len(a) -1
    if low == None:
        low = 0
    if low < high:
        b = a[low:high+1]
        i = b.index(min(b))+low
        swap(a, low, i)
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
            badqsort(a, low, m-1)
        badqsort(a, m+1, high)

def isSorted(a):
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    print("Info: ")
    print(sys.getrecursionlimit())
    ia = [45,65,34,82,30,22]
    print(ia)
    badqsort(ia)
    print(ia)

    dd = [45.0,65.0,34.0,82.0,30.0,22.0]
    print(dd)
    badqsort(dd)
    print(dd)

   # import random

    a = [0]*10000
    for i in range(10000):
        a[i] = random.randint(0,10000)
    print("a gegenereerd")
    print(a[500:510])
    b = list(a)

    import timeit
    timer = timeit.default_timer

    t1 = timer()
    badqsort(a)
    print(a[500:510])
    t2 = timer()
    print(t2-t1)
    print(isSorted(a))

    b.sort()
    print(a == b)
