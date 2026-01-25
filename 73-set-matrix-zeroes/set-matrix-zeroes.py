class Solution(object):
    def setZeroes(self, matrix):

        rows=len(matrix)
        col=len(matrix[0])
        row_track=[0 for _ in range(rows)]
        col_track=[0 for _ in range(col)]
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1
        for i in range(rows):
            for j in range(col):
                if(row_track[i]==-1 or col_track[j]==-1):
                    matrix[i][j]=0
        

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        