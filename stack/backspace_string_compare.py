# https://leetcode.com/problems/backspace-string-compare/
def backspaceCompare(s, t):
    def build(string):
        stack = []
        for ch in string:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return "".join(stack)
    return build(s) == build(t)
print(backspaceCompare(['a','b','#'],['a']))
