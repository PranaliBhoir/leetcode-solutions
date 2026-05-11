# Input Array Is Sorted
def twoSum(numbers):
    target = 15
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right +1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
        
    return [-1,-1]
print(twoSum([2,11,13,15]))