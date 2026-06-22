# https://leetcode.com/problems/third-maximum-number/description/
class Solution:
    def thirdMax(self, nums):
        first = second = third = None
        for num in nums:
            if num in (first, second, third):
                continue
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num
        return third if third is not None else first
nums = [3,2,1]
sol = Solution()
print(sol.thirdMax(nums))
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        return nums[0]
"""