def checkBrackets(string):
    stack = []
    for c in string:
        assert c in "<>[]()" and len(string) > 1

    for c in string:
        if c in "<[(":
            stack.append(c)
        else:
            if c == '>' and stack.pop() != '<':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
            elif c == ')' and stack.pop() != '(':
                return False
            # else:
            #     stack.pop()
        #print(stack)
    return len(stack) == 0

print(checkBrackets("((<>))"))
print(checkBrackets("([)]"))
print(checkBrackets("(("))
print(checkBrackets("(()"))
# print(checkBrackets("lol"))
