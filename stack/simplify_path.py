# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path):
        stack =[]
        parts = path.split("/")
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(part)
        return "/" + "/".join(stack)
path = "/home/"
sol = Solution()
print(sol.simplifyPath(path))