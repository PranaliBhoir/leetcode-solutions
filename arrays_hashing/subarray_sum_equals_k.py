# https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution:
    def subarraySum(self, nums, k):
        res = 0
        currSum = 0
        prevSum = {0 : 1}

        for n in nums:
            currSum += n
            diff = currSum - k

            res += prevSum.get(diff, 0)
            prevSum[currSum] = 1 + prevSum.get(currSum, 0)
        return res
nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))