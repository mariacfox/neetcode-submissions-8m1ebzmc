class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, nn in enumerate(nums):
                if i != j and n + nn == target:
                    return [i, j]