def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("*", end= " ")
            else:
                print("-", end= " ")
        print()
    print()

def rsearch(N):
    global a
    global finalResult
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N and a not in finalResult:
                finalResult.append(a)
                a = []
                return True # geschikte a gevonden
            else:
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False

def allrsearch(N):
    while rsearch(N):
        continue

a = [] # a geeft voor iedere rij de kolompositie aan
finalResult = []
t = 0

allrsearch(8)
# print(a)
printQueens(finalResult[-1])
print(finalResult)

# #===========================================================
#
# from itertools import permutations
#
# n = 8
# cols = range(n)
# for vec in permutations(cols):
#     if n == len(set(vec[i]+i for i in cols)) \
#          == len(set(vec[i]-i for i in cols)):
#         print (vec )
