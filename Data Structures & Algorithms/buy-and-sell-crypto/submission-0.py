class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = 100
        highest_price = 0
        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if prices[i] > highest_price:
                highest_price = prices[i]
            difference = prices[i] - lowest_price
            if difference > max_profit:
                max_profit = difference
        print(lowest_price)
        print(highest_price)
        return max_profit