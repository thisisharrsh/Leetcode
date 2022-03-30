class Solution:
    def jump(self, nums: List[int]) -> int:
        
        start = 0
        last = 0
        ans=0

        while(last<len(nums)-1):
            end=0
            for i in range(start,last+1):
                end=max(end,i+nums[i])

            start=last+1 
            last = end 
            ans=ans+1 

        return(ans)
        