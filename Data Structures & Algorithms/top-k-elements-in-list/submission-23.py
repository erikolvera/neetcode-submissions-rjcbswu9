class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for n in nums:
            num_count[n] = num_count.get(n,0) + 1

        sorted_nums= sorted(num_count, key=num_count.get, reverse=True)

        return sorted_nums[:k]