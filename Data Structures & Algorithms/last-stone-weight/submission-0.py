class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # two heaviest stones, "smash"
        # if x == y, delete both; if x < y, delete x; y = y - x
        # continue until only 1 remains

        # use MaxHeap since we want to keep track of max values
        stones = [-s for s in stones] # negate the values
        heapq.heapify(stones) # max heap

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, x - y)

        stones.append(0)
        return abs(stones[0]) # undo negation