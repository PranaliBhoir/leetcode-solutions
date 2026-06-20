# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))

"""
    #using hashmap 
    n = len(nums)
    present = [False] * (n + 1)
    for num in nums:
        present[num] = True
        
    return [i for i in range(1, n + 1) if not present[i]]
"""