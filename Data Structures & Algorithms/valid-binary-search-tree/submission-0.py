# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root is TreeNode, root.left is TreeNode, root.right is TreeNode
        # root.val is Int
        # leaf would be (Int None None)

        return self.validate(float('-inf'), root, float('inf'))


    def validate(self, lower, node, upper):

        if not node:
            return True

        min_val, max_val = lower, upper
        
        return (min_val < node.val < max_val) and self.validate(min_val, node.left, node.val) and self.validate(node.val, node.right, max_val)


    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     left, right = root.left, root.right

    #     if (left.val < root.val < right.val) and self.isValidBST(left) and self.isValidBST(right):
    #         return True

    #     return False
        