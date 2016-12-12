class sepChainHash:
    def __init__(self):
        self.table = []
        for i in range(10):
            self.table.append(set())

    def __repr__(self):
        result = "Hash-table:\n"
        for hash in self.table:
            result += str(hash)+"\n"
        return result

    def search(self, e):
        if e != None:
            if self.table[int(e%len(self.table))]:
                if e in self.table[int(e%len(self.table))]:
                    return True
        return False

    def insert(self, e):
        fulliness = 0
        for key in self.table:
            if key != set():
                fulliness += len(key)
        if fulliness > 0.75*len(self.table):
            self.rehash(len(self.table)*2)
            print("Rehashed")
        self.table[int(e%len(self.table))].add(e)

    def rehash(self, new_len):
        temp = []
        for key in self.table:
            for e in key:
                temp.append(e)
        self.table = []
        for i in range(new_len):
            self.table.append(set())
        for key in temp:
            self.table[int(e%len(self.table))].add(e)
        print(self.table)

    def delete(self, e):
        deleted = False
        if e != None:
            if self.search(e):
                self.table[int(e%len(self.table))] = self.table[int(e%len(self.table))].remove(e)
                if self.table[int(e%len(self.table))] == None:
                    self.table[int(e%len(self.table))] = set()
                print(str(e) + " successfully removed")
            else:
                print(str(e)+ " not in table\n")
        else:
            print(str(e) + " does not exist\n")

if __name__ == "__main__":
    import random
    hash = sepChainHash()
    randlist = []
    for i in range(200):
        r = random.uniform(0, 1000)
        hash.insert(r)
        randlist.append(r)
    print(hash)

    for i in range(100):
        hash.delete(randlist[50+i])
    print(hash)
