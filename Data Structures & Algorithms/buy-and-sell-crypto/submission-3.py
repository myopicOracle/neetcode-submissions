class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            daily_profit = prices[sell] - prices[buy] 

            if daily_profit > 0:
                max_profit = max(max_profit, daily_profit)
            else:
                buy = sell

            sell += 1

        return max_profit


        # while sell < len(prices):

        #     if prices[buy] < prices[sell]:
        #         daily_profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit, daily_profit)
        #     else:
        #         buy = sell

        #     sell += 1