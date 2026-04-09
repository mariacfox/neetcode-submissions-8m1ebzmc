class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def steps(i):
            if i >= n:
                return i == n
            return steps(i + 1) + steps(i + 2)

        return steps(0)