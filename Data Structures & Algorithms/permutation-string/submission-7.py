class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        counts2 = [0] * 26

        for c in s1:
            index = ord(c) - ord('a')
            counts1[index] +=1

        l=0

        for r in range(len(s2)):
            if counts1 == counts2:
                return True

            index = ord(s2[r]) - ord('a')
            counts2[index] +=1

            if r-l+1 > len(s1):
                counts2[ord(s2[l]) - ord('a')] -=1
                l+=1
        return counts1 == counts2
