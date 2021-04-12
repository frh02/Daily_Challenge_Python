'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.
'''
#SOLUTION:
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans, a, z = [0] * n, 1, k + 1
        for i in range(k+1):
            if i % 2:
                ans[i] = z
                z -= 1
            else:
                ans[i] = a
                a += 1
        for i in range(k+1,n):
            ans[i] = i + 1
        return ans
