class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            maxprofit = max(maxprofit, profit)

            min_price = min(min_price, prices[i])

        return maxprofit