# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2 :
            return None
        
        if t1 :
            v1 = t1.val
            L1 = t1.left
            R1 = t1.right
        else :
            v1 = 0
            L1 = None
            R1 = None
        if t2 :
            v2 , L2 , R2 = t2.val , t2.left , t2.right
        else :
            v2 , L2 , R2 = 0 , None , None
            
        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node