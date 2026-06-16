# https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
nums = [1,2,3,4]
sol = Solution()
print(sol.runningSum(nums))