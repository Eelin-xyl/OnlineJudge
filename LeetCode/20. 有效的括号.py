def isValid(s: str):
    if len(s) % 2 != 0:
        return False
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ')' and stack[-1] != '(':
                return False
            if i == ']' and stack[-1] != '[':
                return False
            if i == '}' and stack[-1] != '{':
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


s = "){"

print(isValid(s))
