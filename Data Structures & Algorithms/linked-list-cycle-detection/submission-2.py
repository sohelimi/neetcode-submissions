# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head of the linked list
        # slow moves 1 step at a time, fast moves 2 steps at a time
        slow = head
        fast = head
        
        # Continue looping while fast pointer and its next node exist
        # We check fast.next to ensure fast can safely move 2 steps
        while fast and fast.next:
            # Move slow pointer one step forward
            slow = slow.next
            # Move fast pointer two steps forward
            fast = fast.next.next

            # If slow and fast pointers meet, we've found a cycle
            # This is because in a cycle, the fast pointer (moving 2 steps)
            # will eventually "lap" the slow pointer (moving 1 step)
            if slow == fast:
                return True
        
        # If the loop completes without pointers meeting,
        # fast reached the end of the list, meaning no cycle exists
        return False
'''Key insight: This uses Floyds Cycle Detection Algorithm (tortoise and hare):

slow pointer: moves 1 node per iteration
fast pointer: moves 2 nodes per iteration
If a cycle exists, the fast pointer will eventually catch up to and meet the slow pointer inside the cycle. If no cycle exists, the fast pointer reaches None and the loop exits.

Time Complexity: O(n) - in worst case, we traverse the entire list
Space Complexity: O(1) - only using two pointers, no extra data structures

Your code is correct! ✓
'''

