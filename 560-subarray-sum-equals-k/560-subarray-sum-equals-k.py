class Solution:
    def subarraySum(self, arr: List[int], Sum: int) -> int:
        
        from collections import defaultdict
        n=len(arr)
        prevSum = defaultdict(lambda : 0)
        res = 0
        currsum = 0
        for i in range(0, n):
            currsum += arr[i]
            if currsum == Sum:
                res += 1		
            if (currsum - Sum) in prevSum:
                res += prevSum[currsum - Sum]
            prevSum[currsum] += 1

        return res
