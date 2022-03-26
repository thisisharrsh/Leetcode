class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res=sum(nums[:3])
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