class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(prices == sorted(prices,reverse = True)):
            return 0
        profit = 0
        maxpro = 0
        min_index = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
            else:
                profit = prices[i] - prices[min_index]
                maxpro = max(maxpro, profit)
        for j in range(min_index+1, len(prices)):
            profit = prices[j] - prices[min_index]
            maxpro = max(maxpro, profit)
        return maxpro

