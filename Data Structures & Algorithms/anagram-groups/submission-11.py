class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = {}
            for c in word:
                count[c] = count.get(c,0)+1

            key = tuple(sorted(count.items()))

            if key not in group:
                group[key] = []

            group[key].append(word)
        return list(group.values())