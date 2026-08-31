class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        l,r = 0,len(xs)-1

        while l < r:
            if xs[r] != xs[l]:
                return False
            l+=1
            r-=1
        return True