class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp=""
        for i in range(len(digits)):
            temp=temp+str(digits[i])

        res=int(temp)+1 
        res1=list(map(int,str(res)))
        return(res1)
        