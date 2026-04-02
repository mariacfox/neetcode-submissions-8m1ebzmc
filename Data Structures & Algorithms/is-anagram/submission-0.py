class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {c: s.count(c) for c in set(s)} == {c: t.count(c) for c in set(t)}
        