class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)-1
        for j in range(n):
            if prices[j]<prices[j+1]:
                    profit+=prices[j+1]-prices[j]
        return profit




            
            
                
