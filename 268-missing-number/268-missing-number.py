class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x=x^i
        for i in range(len(nums)):
            x=x^i
        x=x^(i+1)
        return(x)
    