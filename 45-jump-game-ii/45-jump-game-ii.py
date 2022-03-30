class Solution:
    def jump(self, nums: List[int]) -> int:
        
        currmax = 0
        currreach = 0 
        jumps = 0 
        
        for i in range(len(nums)-1):
            if (i+nums[i] > currmax):
                currmax=i+nums[i]
                
            if i == currreach:
                jumps=jumps+1 
                currreach = currmax
                
        return jumps