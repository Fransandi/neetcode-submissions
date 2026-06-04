class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Edge case: prices list is empty
        if not len(prices):
            return 0

        buy = prices[0]
        sell = prices[0]
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
                sell = 0
            
            sell = max(sell, price)
            profit = max(profit, sell-buy)
            
        return profit

    
        