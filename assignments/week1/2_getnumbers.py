def getNumbers(s):
    result = []
    check = False
    counter = -1
    for c in s:
        if c >= "0" and c <= "9":
            if not check:
                counter += 1
                result.append(c)
            else:
                result[counter] += c
            check = True
        else:
            check = False
    return result

print(getNumbers("een123zin45 6met-632meerdere+7777getallen"))
