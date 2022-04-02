class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        verticalCuts.sort()
        horizontalCuts.sort()
        
        max_hori = -1
        max_vert = -1
        
        for i in range(1,len(verticalCuts)):
            max_vert = max(max_vert, verticalCuts[i] - verticalCuts[i-1])
        
        for j in range(1,len(horizontalCuts)):
            max_hori = max(max_hori, horizontalCuts[j] - horizontalCuts[j-1])
            
        return (max_hori*max_vert) % ((10**9)+7)
            
            