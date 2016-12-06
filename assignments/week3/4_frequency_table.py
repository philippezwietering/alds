def fileToLib(filename):
    with open(filename, 'r') as file:
        dic = {}
        for line in file:
            for word in line.split():
                for char in word:
                    if char in ".?!:;,'\"":
                        word = word.replace(char, '')
                if word in dic.keys():
                    dic[word] += 1
                else:
                    dic[word] = 1
        return dic

def libToFile(filename, dic):
    assert type(dic) == dict
    with open(filename, 'w') as file:
        file.write("This is "+filename+". Size of the dictionary is: "+str(len(dic))+"\n")
        for key in dic.keys():
            file.write("Word: "+str(key)+", number of occurrences: "+str(dic[key])+".\n")

class TrieNode:
    def __init__(self, element=None, occurrence=0):
        self.element = element
        self.occurrence = occurrence

    def __repr__(self, n=0):
        result = ""
        if self.occurrence > 0:
            #TODO




            
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
                    if char in ".?!:;,'\"":
                        word = word.replace(char, '')
                t.insert(word)
        return t

def TrieToFile(filename, t):
    with open(filename, 'w') as file:
        file.write("This is "+filename+".\n")
        file.write(t)

if __name__ == '__main__':
    ####################################
    #   With a dictionary
    ####################################
    # testDict = fileToLib("inputText.txt")
    # libToFile("outputText.txt", testDict)

    ####################################
    #   With a trie
    ####################################
