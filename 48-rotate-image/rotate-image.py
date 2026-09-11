class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        tr_matrix=[[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                tr_matrix[i][j]=matrix[j][i]
        for a in tr_matrix:
            a.reverse()
        for i in range(row):
            for j in range(col):
                matrix[i][j]=tr_matrix[i][j]
        
        return matrix