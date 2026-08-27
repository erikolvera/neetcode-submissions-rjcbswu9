class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = ans = 0

        # for right in range(len(prices)):
        #     profit = prices[right] - prices[left]

        #     if prices[left] > prices[right]:
        #         left = right

        #     ans = max(ans, profit)

        # return ans

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit