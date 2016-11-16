import random

def checkDoubleBirthday(n, tries):
    birthdayOdds = []
    for x in range(tries):
        birthdayList = []
        for i in range(n):
            birthdayList.append(random.randint(1, 365))
            if(len(birthdayList) != len(set(birthdayList))):
                birthdayOdds.append(len(birthdayList))
                break
    # print(birthdayOdds)
    result = len(birthdayOdds)/tries
    return result

print(checkDoubleBirthday(23, 10000))
