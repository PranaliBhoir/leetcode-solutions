# https://leetcode.com/problems/move-zeroes/description/
def moveZeroes(nums):
    left = 0 
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
    return nums
print(moveZeroes([0,1,2,3,0,12]))