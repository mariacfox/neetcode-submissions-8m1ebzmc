# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        if n == 0:
            return []
        res = [pairs[:]]
        
        for i in range(1, n):
            insert_key = pairs[i]
            j = i-1
            while j>= 0 and pairs[j].key > insert_key.key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = insert_key
            res.append(pairs[:])

        return res