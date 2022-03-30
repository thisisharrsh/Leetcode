class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if k>= len(cardPoints):
            return (sum(cardPoints))
        cardPoints = cardPoints[:k] + cardPoints[-k:] # array changed here
        add_k = 0 # include ith element 
        sub_k = 0 # exclude (k+i)th element
        left_k = sum(cardPoints[:k]) # sum of Left most k element
        right_k = sum(cardPoints[-k:]) # sum of right most k element
        maxsum = max(left_k, right_k) # possible max value

        for i in range(k):
            add_k += cardPoints[i]
            sub_k += cardPoints[k+i]
            print(sub_k)
            maxsum = max(right_k - sub_k + add_k, maxsum)
            
        return maxsum
