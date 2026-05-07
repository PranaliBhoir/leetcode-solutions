#https://leetcode.com/problems/two-sum/description/
def two_sum(nums, target):
    seen = {}


    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed],i]
        seen[nums[i]] = i #store the index of the current number in the seen dictionary

print(two_sum([2, 7, 11, 15], 9))
