def intToBinString(n):
    assert n >= 0 and type(n) == int

    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return intToBinString(n//2) + str(n%2)

print(intToBinString(0))
print(intToBinString(1))
print(intToBinString(100))
print(intToBinString(255))
print(intToBinString(2**100))
