# profit = sell day - buy day
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    smallest = min(prices)
    print(smallest)
    index = prices.index(smallest)
    print(index)
    #for i in range(index, len(prices)):


prices_list = [7,1,5,3,6,4]
maxProfit(prices_list)
