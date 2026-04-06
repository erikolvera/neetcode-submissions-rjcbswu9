class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for c in strs:
            key = tuple(sorted(c))
            group[key].append(c)
        return list(group.values())