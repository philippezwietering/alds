import random

def to32bitshash(randomvalue):
    return(hash(randomvalue)%(2**32))


hashdict = dict()
while(True):
    r = random.random()
    if r not in hashdict.values():
        hr = to32bitshash(r)
        if hr in hashdict.keys():
            print(repr(r) + ", " + repr(hashdict[hr]) + ": " + repr(hr))
            break
        hashdict[hr] = r
