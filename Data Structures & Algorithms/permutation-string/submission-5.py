class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            index = ord(c) - ord('a')
            count1[index] += 1

        l = 0
        for r in range(len(s2)):
            if count1 == count2: return True

            index = ord(s2[r]) - ord('a')
            count2[index] += 1

            if r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return count1 == count2
