class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        res = []
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move the right boundary left
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up
            
            if left <= right: 
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move the left boundary right
        
        return res
