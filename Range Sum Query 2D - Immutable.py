'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''
#Solution
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ylen, xlen = len(matrix) + 1, len(matrix[0]) + 1
        self.dp = [[0] * xlen for _ in range(ylen)]
        for i in range(1, ylen):
            for j in range(1, xlen):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    
       

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
