class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]

            if prices[left] > prices[right]:
                left = right

            ans = max(ans, profit)

        return ans