class Solution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))

            else:
                stack.append(int(token))

        return stack[0]
tokens = ["4","13","5","/","+"]
sol = Solution()
print(sol.evalRPN(tokens))