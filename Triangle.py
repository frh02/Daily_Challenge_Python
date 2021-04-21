'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''
##SOLUTION##
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        memo = [None] * len(triangle)
        n = len(triangle) - 1
     
        # For the bottom row
        for i in range(len(triangle[n])):
            memo[i] = triangle[n][i]
 
        # Calculation of the
        # remaining rows,
        # in bottom up manner.
        for i in range(len(triangle) - 2, -1,-1):
            for j in range( len(triangle[i])):
                memo[j] = triangle[i][j] + min(memo[j],
                                        memo[j + 1]);
 
        # return the top element
        return memo[0]
