class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) -1
        while left<=right:
            mid = left + (right-left) //2

            if nums[mid] == target:
                return mid

            if (nums[left] <= target <= nums[mid]
                or nums[mid] < nums[right] < target
                or target< nums[mid] < nums[right]):
                right = mid
            else:
                left = mid +1
        return -1


