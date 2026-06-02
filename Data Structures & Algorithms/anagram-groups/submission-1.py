class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            sortedd = ''.join(sorted(word))
            ans[sortedd].append(word)
        return list(ans.values())

        