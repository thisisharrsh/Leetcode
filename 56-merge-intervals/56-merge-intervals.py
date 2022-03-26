class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def ismerge(i,j):
            x=max(i[0],j[0])
            y=min(i[1],j[1])

            return y-x >=0
        
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for i in intervals[1:]:
            j=res[-1]

            if ismerge(i,j):
                merger1=min(i[0],j[0])
                merger2=max(i[1],j[1])
                res[-1]=[merger1,merger2]

            else:
                res.append(i)

        return(res)
    
    
        
