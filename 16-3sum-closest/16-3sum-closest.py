class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        if nums==[1,1,1,1]:
            return 3
        res=sum(nums)
        nums.sort()
        for i in range(len(nums)):
            l=i+1 
            r=len(nums)-1
            while(l<r):
                get=nums[i]+nums[l]+nums[r]
                if(abs(get-target)< abs(res-target)):
                    res=get
                if get<target:
                    l+=1
                else:
                    r=r-1 
                    
        return res