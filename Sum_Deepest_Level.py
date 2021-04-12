'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    #using depth first search find the node with the deepest level 
        def dfs1(node):
            if not node: return 0
            return max(dfs1(node.left), dfs1(node.right)) + 1
   #define a method which will check if the current node is the deepest level or not 
        def dfs2(node, d):
            if not node: return
            if d == depth: self.ans += node.val
            dfs2(node.left, d+1)
            dfs2(node.right, d+1)
     
        self.ans = 0
        depth = dfs1(root)
        dfs2(root, 1)
        return self.ans
        
