class Solution:
    def isValid(self, s: str) -> bool:
        h = {'}':'{',')':'(',']':'['}
        stack = []
        for c in s:
            if c not in h:
                stack.append(c)
            elif not stack or stack[-1]!= h[c]:
                return False
            else:
                stack.pop()
        return not stack