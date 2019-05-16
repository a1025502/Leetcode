# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def tBST(node):
            if node is None:
                return None
            if node.val > R:
                return tBST(node.left) #find < R value
            if node.val < L:
                return tBST(node.right)
            
            node.left,node.right = tBST(node.left),tBST(node.right)
            return node
        
        return tBST(root)