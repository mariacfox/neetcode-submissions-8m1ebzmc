class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) > len(set(nums)) else False