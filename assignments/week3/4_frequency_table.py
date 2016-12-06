def fileToLib(filename):
    with open(filename, 'r') as file:
        dic = {}
        for line in file:
            for word in line.split():
                for char in word:
                    if char in ".?!:;,()'\"":
                        word = word.replace(char, '')
                if word in dic.keys():
                    dic[word] += 1
                else:
                    dic[word] = 1
        return dic

def libToFile(filename, dic):
    assert type(dic) == dict
    with open(filename, 'w') as file:
        file.write("This is "+filename+". Number of words is: "+str(len(dic))+"\n")
        for key in dic.keys():
            file.write(str(key)+": "+str(dic[key])+"\n")

class TrieNode:
    def __init__(self, element=None, occurrence=0):
        self.element = element
        self.occurrence = occurrence

    def __repr__(self, n=""):
        result = ""
        if self.occurrence > 0:
            result += n+": "+str(self.occurrence)+"\n"
        if self.element != None:
            for key in self.element:
                result += self.element[key].__repr__(n+key)
        return result

    def size(self):
        result = 0
        if self.occurrence > 0:
            result += 1
        if self.element != None:
            for key in self.element:
                result += self.element[key].size()
        return result

    def insert(self, e):
        if e:
            if self.element:
                if e[0] in self.element.keys():
                    self.element[e[0]].insert(e[1:])
                else:
                    self.element[e[0]] = TrieNode()
                    self.element[e[0]].insert(e[1:])
            else:
                self.element = {e[0]: TrieNode()}
                self.element[e[0]].insert(e[1:])
        else:
            self.occurrence += 1

class Trie:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root:
            return self.root.__repr__()
        else:
            return "null-trie"

    def size(self):
        if self.root != None:
            return self.root.size()
        else:
            return 0

    def insert(self, e):
        if self.root:
            return self.root.insert(e)
        else:
            self.root = TrieNode()
            self.root.insert(e)

def fileToTrie(filename):
    with open(filename, 'r') as file:
        t = Trie()
        for line in file:
            for word in line.split():
                for char in word:
                    if char in ".?!:;,()'\"":
                        word = word.replace(char, '')
                t.insert(word)
        return t

def TrieToFile(filename, t):
    with open(filename, 'w') as file:
        file.write("This is "+filename+". Number of words is: "+str(t.size())+"\n")
        file.write(t.__repr__())

if __name__ == '__main__':
    ####################################
    #   With a dictionary
    ####################################
    testDict = fileToLib("inputText.txt")
    libToFile("outputText.txt", testDict)

    ####################################
    #   With a trie
    ####################################
    testTrie = fileToTrie("inputText.txt")
    TrieToFile("trietext.txt", testTrie)
