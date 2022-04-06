class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        count1, count2, m1, m2 = 0, 0, 0, 1
        for n in nums:
            if n == m1:
                count1 += 1
            elif n == m2:
                count2 += 1
            elif count1 == 0:
                m1, count1 = n, 1
            elif count2 == 0:
                m2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (m1, m2) if nums.count(n) > len(nums) // 3]
        