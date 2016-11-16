def next_las_seq(x):
    assert len(x) > 0
    result = []
    l = len(x)
    counter = 1
    lastNumber = x[0]
    if l > 1:
        for i in range(1, l):
            if lastNumber == x[i]:
                # print("ouwe")
                counter += 1
            else:
                # print("Nieuw")
                result.append(counter)
                result.append(lastNumber)
                counter = 1
                lastNumber = x[i]
        result.append(counter)
        result.append(lastNumber)

    else:
        result = [counter, lastNumber]
    return result

def iterate_las(x, n):
    print(x)
    for i in range(n):
        x = next_las_seq(x)
        print(x)

x = [3, 3, 4, 1, 1, 6, 6, 6, 1]
iterate_las(x, 2)
iterate_las([1], 5)
