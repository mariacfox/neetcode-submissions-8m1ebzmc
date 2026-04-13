class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # pairs defined above
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, pairs, left, right):
        if right - left + 1 <= 1: # if len <= 1
            return 

        pivot = pairs[right] #right-most
        pointer = left

        for i in range(left, right):
            # partition
            if pairs[i].key < pivot.key:
                tmp = pairs[pointer]
                pairs[pointer] = pairs[i]
                pairs[i] = tmp
                pointer += 1

        pairs[right] = pairs[pointer]
        pairs[pointer] = pivot

        self.quickSortHelper(pairs, left, pointer - 1)
        self.quickSortHelper(pairs, pointer + 1, right)