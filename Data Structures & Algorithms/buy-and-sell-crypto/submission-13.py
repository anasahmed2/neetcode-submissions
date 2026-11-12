class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = float('inf')

        profit = 0

        for price in prices:

            if price < buy_price:

                buy_price = price 

            current_profit = price - buy_price

            if current_profit > profit:

                profit = current_profit


        return profit