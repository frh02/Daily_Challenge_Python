'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.


'''

#solution:
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        g = local = 0
        for i in range(1, n):
            if A[i] < A[i-1]:                   # Calculate local inversion
                local += 1
            if A[i] < i:                        # Calculate global inversion
                diff = i - A[i]                 # diff = actual_index index_this_value_is_supposed_to_have_if_the_list_is_in_order
                g += diff * (diff+1) // 2       # see explanation for this formula from `Explanation` section
        return g == local
