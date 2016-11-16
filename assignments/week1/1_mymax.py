import math
def mymax(a):
    assert len(a) > 0
    highest = a[0]
    for element in a:
        assert type(element) == int or type(element) == float
        if element > highest:
            highest = element
    return highest

print(mymax([1, math.inf, 2, 3, 4]))
