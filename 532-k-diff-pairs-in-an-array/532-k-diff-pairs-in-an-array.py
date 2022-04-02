class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        temp=collections.Counter(nums)
        
        ans=0 
        
        for i in temp:
            if ((k>0 and i-k in temp) or (k<=0 and temp[i]>1)):
                ans+=1
                
        return ans
        