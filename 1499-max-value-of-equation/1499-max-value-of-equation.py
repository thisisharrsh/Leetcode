class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        maxi = float("-inf")
        heap=[]
        heapq.heapify(heap)
        for i in range(len(points)):
            while len(heap)>0 and abs(heap[0][1] - points[i][0])>k:
                heapq.heappop(heap)
            if len(heap)>0:
                maxi = max(maxi, -heap[0][0]+points[i][0] + points[i][1])
            heapq.heappush(heap,(-points[i][1] + points[i][0],points[i][0]))
            
        return maxi 
        