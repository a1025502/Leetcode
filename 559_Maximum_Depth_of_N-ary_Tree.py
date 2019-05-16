"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if node is None:
                return 0
            ans = 0
            for i in node.children:
                ans = max(dfs(i),ans)
            return ans+1
        
        return dfs(root)
  