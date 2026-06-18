# https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            if count[num] > len(nums) // 2:
                return num
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))

'''
#Boyer- moore 
        count = 0
        candidate = None

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
'''