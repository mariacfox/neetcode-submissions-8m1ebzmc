# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)                     # number of pairs to sort
        if n == 0:                         # handle empty input early
            return []
        
        res = [pairs[:]]                    # snapshot initial state (copy of array)
        
        for i in range(1, n):                # outer loop: insert element at i
            insert_key = pairs[i]            # the element we want to place into the sorted portion
            j = i - 1                        # start comparing with the element on the left
            
            # shift elements to the right while they are greater than the insert_key
            while j >= 0 and pairs[j].key > insert_key.key:
                pairs[j + 1] = pairs[j]        # move left element one position to the right
                j -= 1                          # move left to check the next element
            
            pairs[j + 1] = insert_key            # place the key into its correct position
            
            res.append(pairs[:])                 # snapshot after this insertion (copy)
        
        return res