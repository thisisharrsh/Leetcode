class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ans=0 
        temp={}
        
        for i in nums:
            if i not in temp:
                temp[i] = 1 
            else:
                temp[i]+=1
        
        for i in temp:
            if ((k>0 and i-k in temp) or (k<=0 and temp[i]>1)):
                ans+=1
                
        return ans
        