'''
input m x n matric of ints. 
* NOT nxn
- if an element is 0, set its entire row and column to 0's.
- You must update the matrix in-place
Follow up: Could you solve it using O(1) space?

Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]

Naive:
O(nxm) pass over all cells
- for each, O(n + m) pass to set all to 0
overal (nxm)*(n + m) which is roughly n*2 * n (if n is bigger) = O(n^3)

Insight:
Once we've cleared a row or a col, we never have to traverse it again
Or said differently, we only need to clear a given row / col ONCE

What if we did:
O(nxm) pass over all cells, maintain 2 sets, row and col #s to clear
At worst, that is every row and every col, which is O(m + n) clear operations
- a clear operation is ~O(n) (if n > m)
- we still have O(n) * O(n) = O(n*2) time



'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_clear, cols_to_clear = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_to_clear.add(i)
                    cols_to_clear.add(j)

        for row_idx in rows_to_clear:
            matrix[row_idx] = [0] * len(matrix[row_idx])

        for col_idx in cols_to_clear:
            for row in range(len(matrix)):
                matrix[row][col_idx] = 0


        






