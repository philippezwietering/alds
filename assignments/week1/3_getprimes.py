def getPrimes(n):
    primes = [2]
    for i in range(3, n+1):
        # print(i)
        check = 0
        for p in primes:
            # print(p)
            # print(i % p)
            if i % p != 0:
                check += 1
            else:
                break
        if check == len(primes):
            primes.append(i)
    return primes

output = getPrimes(1000000)
for x in output:
    print(x)
