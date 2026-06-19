# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums):
        seen = set(nums)
        for i in range(len(nums) + 1):
            if i not in seen:
                return i
nums = [3,0,1]
sol = Solution()
print(sol.missingNumber(nums))