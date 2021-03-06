def powerv1(a, n):
    return a**n

def powerv2(a, n):
    assert n > 0
    m = 1
    for _ in range(0, n):
        m *= a
    return m

def powerv3(a, n):
    assert n > 0
    x = 0
    m = 1
    while n > 0:
        if n%2 == 0:
            a *= a
            x += 1
            n /= 2
        else:
            m *= a
            n -= 1
            x+= 1
    print(x)
    return m

print(powerv3(2, 10000))
#print(2**10000)
