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
        if e in self.table[int(e%len(self.table))]:
            return e%len(self.table)
        else:
            return None

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
        # print(self.table)

if __name__ == "__main__":
    import random
    hash = sepChainHash()
    for i in range(200):
        hash.insert(random.uniform(0, 1000))
    print(hash)
