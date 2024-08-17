class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        curr_min_price = prices[0]
        
        max_profit = 0
        
        for price in prices:
            
            # Calculating the curr_profit
            curr_profit =  price - curr_min_price
            
            # Updating the profit
            max_profit = max(max_profit,curr_profit)
            
            # Updating the min_price for stock
            curr_min_price = min(curr_min_price,price)
            
        return max_profit