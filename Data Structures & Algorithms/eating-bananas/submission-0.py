class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            print(f"Mid is {mid}")

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
                print(f"totalTime at {p} piles: {totalTime}")
            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res