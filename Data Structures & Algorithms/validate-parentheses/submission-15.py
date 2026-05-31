class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}": "{", "]":"[", ")": "("}

        for c in s:
            if c not in dic:
                stack.append(c)
            elif not stack or stack[-1] != dic[c]:
                return False
            else:
                stack.pop()
        return not stack
