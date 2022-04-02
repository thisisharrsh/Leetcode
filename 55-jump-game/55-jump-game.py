class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        res = 0
        ans = True
        for i in range(len(nums)):
            res = max(res-1, nums[i])
            if res==0 and i!=len(nums)-1:
                ans = False
                break
        return(ans)
        