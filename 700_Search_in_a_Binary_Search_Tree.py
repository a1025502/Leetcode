# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        ans = root
        while ans:
            if ans.val == val:
                return ans
            elif ans.val > val :
                ans = ans.left
            else :
                ans = ans.right