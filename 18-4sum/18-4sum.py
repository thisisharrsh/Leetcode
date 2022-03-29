class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def ksum(k, strt, target):
            if k != 2:
                for i in range(strt, len(nums) - k + 1):         
                    if i > strt and nums[i] == nums[i-1]:       
                        continue 
                    quad.append(nums[i])
                    ksum(k-1, i + 1, target - nums[i])
                    quad.pop()
                return 

            l, r = strt, len(nums)-1       
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        nums.sort()         
        res, quad = [], []
        ksum(4, 0, target)
        return (res)
