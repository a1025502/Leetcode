# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def LST(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            ans = []
            ans += LST(root.left)
            ans += LST(root.right)
            
            return ans
        
        ans1 = LST(root1)
        ans2 = LST(root2)
        
        return ans1 == ans2