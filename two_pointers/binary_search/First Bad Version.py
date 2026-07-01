# https://leetcode.com/problems/first-bad-version/description/
first_bad = 4

def isBadVersion(version):
    return version >= first_bad

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
sol = Solution()
print(sol.firstBadVersion(5))