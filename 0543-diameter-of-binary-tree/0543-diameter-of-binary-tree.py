# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 

        def height(node):
            if node is None:
                return -1 #return -1 edges

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter , left_height + right_height +2 ) #updating diameter because path through current node = left + right
            return 1 + max(left_height, right_height)


        height(root) #run dfs again to compute heights and update diameter
        return self.diameter 