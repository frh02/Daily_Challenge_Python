'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''
#SOLUTION#
######################################################################################################################################


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = left = right = 0
        
        for i in s:
            if i=='(':
                left += 1
            else:
                right += 1
            if left == right:
                m = max(m, right+left)
            elif right>left :
                left = right = 0
                
        left = right=0
        
        for i in s[::-1]:
            if i ==')':
                right += 1
            else:
                left += 1
            if left == right:
                m = max(m,right+left )
            elif left >right:
                left =right=0

        return m
