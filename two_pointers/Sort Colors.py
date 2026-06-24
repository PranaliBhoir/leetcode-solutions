# https://leetcode.com/problems/sort-colors/description/
# Dutch National Flag Algorithm
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        current = 0
        right = len(nums) - 1
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
        return nums
nums = [2,0,2,1,1,0]
sol = Solution()
print(sol.sortColors(nums))