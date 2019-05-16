"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        if not root.children:
            return [root.val]
        ans = []
        
        for i in root.children:
            ans = ans + self.postorder(i)
            
        ans += [root.val]
        return ans