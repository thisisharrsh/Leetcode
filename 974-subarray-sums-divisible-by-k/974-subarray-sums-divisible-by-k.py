class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        res = {0: 1}
        Sum = 0
        count = 0
        for i in range(len(nums)):
            Sum = (Sum + nums[i]) % k
            if Sum < 0:
                Sum += k
            if Sum in res:
                count += res[Sum]
            if Sum not in res:
                res[Sum] = 0
            res[Sum] += 1
        return count