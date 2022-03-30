class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def backtracking(comb, pre, start):
            if not candidates or pre > target:
                return
            if pre == target:
                ans.append(comb)
                return
            for i in range(start, len(candidates)):
                backtracking(comb + [candidates[i]], pre + candidates[i], i)
            
        backtracking([], 0, 0)
        return ans
        