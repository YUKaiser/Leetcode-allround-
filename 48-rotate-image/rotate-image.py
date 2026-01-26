class Solution(object):
    def rotate(self, matrix):
        rows=len(matrix)
        col=len(matrix[0])
        for i in range(rows-1):
            for j in range(i+1,col):
                if(i!=j):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(rows):
            matrix[i].reverse()

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        