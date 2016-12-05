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

if __name__ == '__main__':
    print(fileToLib("text.txt"))
