# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (like removing head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = dummy
        slow = dummy

        # Step 1: Move 'fast' pointer n+1 steps ahead
        # This creates a gap of n between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Step 2: Move both pointers until fast reaches the end
        # Now slow will be just before the node we want to remove
        while fast:
            fast = fast.next
            slow = slow.next

        # Step 3: Remove the nth node from end
        # Skip the target node
        slow.next = slow.next.next

        # Return the updated list (skip dummy)
        return dummy.next