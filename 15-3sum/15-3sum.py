class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        set1 = set()
        nums.sort()

        for i in range(len(nums)):
            get = -nums[i]
            j = i+1
            k=len(nums)-1
            while j < k:
                find = nums[j] + nums[k]
                if find == get and (nums[j],nums[k]) not in set1:
                    res.append([nums[i],nums[j],nums[k]])
                    set1.add((nums[j],nums[k]))
                if find > get:
                    k -= 1
                else:
                    j+=1
        return(res)

                    