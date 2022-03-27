class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1]<nums[i]:
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[i-1]<nums[j]:
                break

        if i!=0 and j!=0:
            nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]
        return(nums)
