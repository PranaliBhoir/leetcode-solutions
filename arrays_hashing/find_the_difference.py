# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s, t):
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1
s = "abcd"
t = "abcde"
sol = Solution()
print(sol.findTheDifference(s, t))