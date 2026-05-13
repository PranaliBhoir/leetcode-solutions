# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def removeDuplicates(nums):
    if not nums:
        return 0     
    left = 0

    for right in range(1, len(nums)):

        if nums[left] != nums[right]:

            left += 1
            nums[left] = nums[right]

    return left + 1
print(removeDuplicates([1,1,2]))