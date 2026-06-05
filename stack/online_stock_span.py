# https://leetcode.com/problems/online-stock-span/description/
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):

        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span


# Create object
stockSpanner = StockSpanner()

# Test prices
print(stockSpanner.next(100))  # 1
print(stockSpanner.next(80))   # 1
print(stockSpanner.next(60))   # 1
print(stockSpanner.next(70))   # 2
print(stockSpanner.next(60))   # 1
print(stockSpanner.next(75))   # 4
print(stockSpanner.next(85))   # 6