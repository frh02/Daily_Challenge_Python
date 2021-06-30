'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

#SOLUTION:

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        trav, i = 0, 0
        c = 0
        maximum = 0
        n= len(nums)
 
    # Iterate unil n-k+1 as we
    # have to go till i+k
        while i < n - k + 1:
            trav = i - 1
            c = 0
 
        # Iterate in the array in left direction
        # till you get 1 else break
            while trav >= 0 and nums[trav] == 1:
                trav -= 1
                c += 1
            trav = i + k
 
        # Iterate in the array in right direction
        # till you get 1 else break
            while (trav < n and nums[trav] == 1):
                trav += 1
                c += 1
 
            c += k
 
        # Compute the maximum length
            if (c > maximum):
                maximum = c
            i += 1
 
    # Return the length
        return maximum
