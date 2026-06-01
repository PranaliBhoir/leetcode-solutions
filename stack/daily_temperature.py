# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer
temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))