# https://leetcode.com/problems/guess-number-higher-or-lower/description/
secret = 6

def guess(num):
    if num == secret:
        return 0
    elif num < secret:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1

sol = Solution()
print(sol.guessNumber(10))