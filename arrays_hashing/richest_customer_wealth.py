# https://leetcode.com/problems/richest-customer-wealth/description/
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for row in accounts:
            wealth = sum(row)
            max_wealth = max(max_wealth, wealth)
        return max_wealth
accounts = [[1,2,3],[3,2,1]]
sol = Solution()
print(sol.maximumWealth(accounts))