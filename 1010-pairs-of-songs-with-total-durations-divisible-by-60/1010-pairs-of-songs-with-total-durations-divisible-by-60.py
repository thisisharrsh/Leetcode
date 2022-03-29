class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        dp=[0]*60
        res = 0
        for duration in time :
            reminder = duration % 60
            target = (60 - reminder) % 60
            res=res + dp[target]
            dp[reminder] +=1 
            
        return res