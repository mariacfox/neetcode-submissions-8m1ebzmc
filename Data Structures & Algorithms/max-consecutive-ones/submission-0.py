class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = ones_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_count += 1
                max_ones = max(max_ones, ones_count)
            else:
                # reset ones_count
                ones_count = 0

        return max_ones