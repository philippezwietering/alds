def function(n):
    assert type(n) == int

    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    a = []
    j = 0
    for munt in m:
        if munt > n:
            break
        a.append([])
        for i in range(n+1):
            if j == 0 or i == 0:
                a[j].append(1)
            elif i >= m[j]:
                a[j].append(a[j-1][i] + a[j][i-m[j]])
            else:
                a[j].append(a[j-1][i])
        j += 1
        #print(a)
    return a[j-1][n]

print(function(50))
