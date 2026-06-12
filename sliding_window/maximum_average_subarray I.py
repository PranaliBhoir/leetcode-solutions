# https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
nums = [1,12,-5,-6,50,3]
k = 4
sol = Solution()
print(sol.findMaxAverage(nums, k))