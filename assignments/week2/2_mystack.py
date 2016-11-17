[2_mystack.py]
class mystack():
    stack = []
    numberOfEntries = 0

    def __init__(self, initialStack = []):
        self.stack = initialStack
        self.numberOfEntries = len(initialStack)

    def __repr__(self):
        return "Size: " + str(self.numberOfEntries) + "\nStack: " + str(self.stack)

    def push(self, n):
        self.stack.append(n)
        self.numberOfEntries += 1

    def pop(self):
        result = self.stack[-1]
        self.stack = self.stack[:-1]
        self.numberOfEntries -= 1
        return result

    def peek(self, n):
        assert -1 < n < self.numberOfEntries
        return self.stack[n]

    def isEmpty(self):
        return self.numberOfEntries > 0


s = mystack()
print(s)
print(s.isEmpty())

for i in range(5):
    s.push(i)
print(s)

for i in range(3):
    print(s.pop())

print(s)
print(s.isEmpty())
