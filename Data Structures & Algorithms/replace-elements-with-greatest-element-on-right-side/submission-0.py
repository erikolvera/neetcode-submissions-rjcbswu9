class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
        #     for j in range(i+1, arr):
        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

        

        # for r in range(len(arr)):
        #     while arr[r] > arr[l]:
        #         arr[l] = arr[r]
        # return arr