def calPoints(operations):
    stack=[]
    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else: 
            stack.append(int(op))
    return sum(stack)
print(calPoints(["1","2","3","C","D","+","+"])) 