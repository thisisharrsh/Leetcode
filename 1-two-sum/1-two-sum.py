class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    m.append(i)
                    m.append(j)
                    break
                else:
                    pass
        
        return(m)
        