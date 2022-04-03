class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices) 
        buy = [-10000]*3
        sell = [0]*3
        
        for i in prices:
            for j in range(1,3):
                buy[j] = max(buy[j],sell[j-1]-i)
                sell[j] = max(sell[j],buy[j]+i)
                
        return(sell[2])
        