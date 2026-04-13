class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])     

        top, bottom = 0, rows-1
        while top <= bottom:
            mid = (top + bottom) // 2
            mid_array = matrix[mid]
            
            if target > mid_array[cols-1]:
                top = mid + 1
            elif target < mid_array[0]:
                bottom = mid - 1
            else:
                # Standard binary search within the identified row
                l, r = 0, cols - 1
                while l <= r:
                    m = (l + r) // 2
                    if mid_array[m] == target:
                        return True
                    elif mid_array[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False