# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        count = 0
        ans = head
        
        while ans :
            count += 1
            ans = ans.next
            
        middle = count/2
        ans = head
        while middle >= 1:
            ans = ans.next
            middle -=1 
        return ans