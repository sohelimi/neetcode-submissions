class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #We can use 2 pointers here, left pointer will track buy 
        #and Right pointer will take care of the sell
        l,r = 0, 1 # we start with 1st and 2nd price in the List
        maxP = 0
        while r < len(prices):
            profit = prices(r) - prices(l)
            if profit > maxP:
                maxP = profit
            else:
                l = r
            r += 1    










'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Brute-force algorithm to find the maximum profit by checking
        every possible pair of buy and sell days.
        
        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum achievable profit. Returns 0 if no profitable transaction.
        """
        max_profit = 0
        n = len(prices)

        # Try every possible pair where buy day < sell day
        for buy in range(n):
            # We can only sell on a day after we buy
            for sell in range(buy + 1, n):  
                profit = prices[sell] - prices[buy]  # Profit for this buy/sell pair
                max_profit = max(max_profit, profit) # Update max_profit if this is better

        # If all pairs yield negative profit, max_profit remains 0 (no transaction is best)
        return max_profit   
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit possible from one buy and one sell of stock.
        
        Approach:
        - Track the minimum price seen so far while iterating through prices.
        - At each step, compute the profit if we bought at the min price and sold at current price.
        - Update the maximum profit as needed.

        Args:
        prices (List[int]): List of stock prices.

        Returns:
        int: The maximum profit achievable, or 0 if none.
        """
        min_price = float('inf')  # Initialize min_price to a very large value
        max_profit = 0            # Initialize max_profit to zero

        for price in prices:
            # Update the min_price if we find a new lower price
            min_price = min(min_price, price)
            # Calculate the profit if we sold at the current price
            profit = price - min_price
            # Update max_profit if this profit is higher than before
            max_profit = max(max_profit, profit)

        return max_profit 