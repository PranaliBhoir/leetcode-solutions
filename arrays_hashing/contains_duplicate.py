#https://leetcode.com/problems/contains-duplicate/description/
def contains_duplicate(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_duplicate([1,2,3,1]))