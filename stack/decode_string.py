# https://leetcode.com/problems/decode-string/description/
class Solution:
    def decodeString(self, s):
        stack =[]
        current = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((current,num))
                current =""
                num = 0
            elif ch == "]":
                prev_string, repeat = stack.pop()
                current = prev_string + current * repeat
            else:
                current += ch
        return current
s = "3[a]2[bc]"
sol = Solution()
print(sol.decodeString(s))