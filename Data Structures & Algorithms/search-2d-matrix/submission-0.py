class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        small_row = 0 
        big_row = len(matrix) - 1

        # immediately know target is not present in matrix
        if target < matrix[small_row][0] or target > matrix[big_row][-1]:
            return False

        row = -1 
        while small_row <= big_row:
            mid = small_row + ((big_row - small_row) // 2)
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            elif matrix[mid][0] > target: # this row is too big
                big_row = mid - 1
            elif matrix[mid][0] < target: # this row is too small
                small_row = mid + 1

        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if matrix[row][mid] == target: 
                return True
            elif matrix[row][mid] > target: 
                right = mid - 1
            elif matrix[row][mid] < target: 
                left = mid + 1

        
        return False