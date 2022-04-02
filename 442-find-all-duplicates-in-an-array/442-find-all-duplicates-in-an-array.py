class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        d={}
        res = []
        nums.sort()

        for i in nums:
            if i not in d:
                d[i]=1 
            else:
                d[i]=d[i]+1 

        for key,value in d.items():
            if value == 2:
                res.append(key)

        return(res)
        