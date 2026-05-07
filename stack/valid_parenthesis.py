def valid_parenthesis(str):
    stack=[]
    pairs={
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for ch in str:
        if ch in pairs:
            if stack and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False
print(valid_parenthesis("([])"))
