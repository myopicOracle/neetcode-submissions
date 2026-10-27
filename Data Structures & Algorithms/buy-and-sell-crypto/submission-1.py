class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            buy = prices[i]

            for j in range(i + 1, len(prices)):
                sell = prices[j]
                daily_profit = sell - buy

                max_profit = max(max_profit, daily_profit)

        return max_profit

        # # Janky Brute
        # max_profit = 0
        # last_day = len(prices) - 1
        
        # buy = 0
        # while buy < last_day:
            
        #     sell = last_day
        #     while sell > buy:
        #         daily_profit = prices[sell] - prices[buy]

        #         max_profit = max(max_profit, daily_profit) 

        #         sell -= 1

        #     buy += 1 
            
        # return max_profit
