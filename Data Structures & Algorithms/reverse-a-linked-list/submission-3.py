# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None      # Tracks the previous node (initially None, will be new tail)
        curr = head      # Pointer to current node we're processing
        
        while curr:      # Traverse until we reach the end of the list
            # Store the next node before we break the link
            temp = curr.next
            
            # Reverse the pointer: point current node back to previous node
            curr.next = prev
            
            # Move prev forward: prev is now at current node
            prev = curr
            
            # Move curr forward: curr is now at the next node
            curr = temp
        
        # prev is now at the last node (new head of reversed list)
        return prev


'''
Iteration 1:
temp = 1
reverse: 0 → None
prev = 0
curr = 1
Iteration 2:
temp = 2
reverse: 1 → 0
prev = 1
curr = 2
Iteration 3:
temp = 3
reverse: 2 → 1
prev = 2
curr = 3
Iteration 4:
temp = None
reverse: 3 → 2
prev = 3
curr = None
'''























'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next   # store next node
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_temp        # move curr forward
        return prev
'''
