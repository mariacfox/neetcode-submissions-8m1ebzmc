class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Copy all n elements from nums2 into nums1 starting at index m.
        nums1[m:] = nums2
        nums1 = nums1.sort()