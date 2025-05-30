class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            ans = "".join(sorted(i))
            hashmap[ans].append(i)
        return list(hashmap.values())