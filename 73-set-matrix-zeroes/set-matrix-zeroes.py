class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_track=[0]*len(matrix)
        col_track=[0]*len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1
        for i in range(row):
            for j in range(col):
                if col_track[j]==-1 or row_track[i]==-1:
                    matrix[i][j]=0
        return matrix