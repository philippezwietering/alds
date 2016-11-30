class mystack(list):
    stack = []

    def __init__(self, initialStack = []):
        self.stack = initialStack

    def __repr__(self):
        return "Size: " + str(len(self.stack)) + "\nStack: " + str(self.stack)

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if not self.isEmpty():
            result = self.stack[-1]
            self.stack = self.stack[:-1]
            return result
        else:
            return None

    def peek(self, n):
        assert -1 < n < len(self.stack)
        return self.stack[n]

    def isEmpty(self):
        return len(self.stack) == 0


s = mystack()
print(s)
print(s.isEmpty())

for i in range(5):
    s.push(i)
print(s)

print("-----------")
for i in range(3):
    print(s.pop())

print(s)
print(s.isEmpty())
