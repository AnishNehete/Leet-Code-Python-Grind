# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val: #both p and q are smaller, both must be in left sub tree
                root =root.left #move root
            elif p.val >root.val and q.val > root.val:
                root = root.right
            else:
                return root