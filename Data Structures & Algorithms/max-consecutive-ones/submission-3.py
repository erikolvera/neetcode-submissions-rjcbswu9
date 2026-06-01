class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_streak = 0

        for n in nums:
            if n == 1:
                counter +=1
                max_streak= max(counter,max_streak)
            else:
                counter = 0
        return max_streak