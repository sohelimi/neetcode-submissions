# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to simplify edge cases (like empty lists)
        dummy = ListNode(0)
        
        # 'tail' will always point to the last node in the merged list
        tail = dummy

        # Traverse both lists while neither is empty
        while list1 and list2:
            
            # Compare values of current nodes
            if list1.val < list2.val:
                # Attach list1 node to merged list
                tail.next = list1
                
                # Move list1 pointer forward
                list1 = list1.next
            else:
                # Attach list2 node to merged list
                tail.next = list2
                
                # Move list2 pointer forward
                list2 = list2.next
            
            # Move the tail forward (very important!)
            tail = tail.next

        # At this point, one of the lists is empty
        # Attach the remaining part of the non-empty list
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return the merged list (skip dummy node)
        return dummy.next
        
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
'''