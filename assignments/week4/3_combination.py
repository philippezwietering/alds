def combination(n, k):
    assert type(n) == int
    assert type(k) == int

    binomium = []
    row = 0
    while n > row-2:
        binomium.append([])
        for i in range(row):
            if row-1 == i or i == 0:
                binomium[row-1].append(1)
            else:
                binomium[row-1].append(binomium[row-2][i-1]+binomium[row-2][i])
        row += 1
    return binomium[n][k]

print(str(combination(100, 50)))
