# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: no lists at all -> nothing to merge
        if not lists or len(lists) == 0:
            return None

        # Repeatedly merge lists in pairs until only one list remains.
        # Round 1: [L0,L1,L2,L3] -> [merge(L0,L1), merge(L2,L3)]
        # Round 2: merge those two results -> single list.
        # This is like building a balanced binary tree of merges,
        # which keeps the total work = O(N log k).
        while len(lists) > 1:
            mergedLists = []
            # Step through the list in chunks of 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # l2 may not exist if there's an odd number of lists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            # Replace the old list of lists with the newly merged ones
            lists = mergedLists

        # Only one merged list remains
        return lists[0]

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Standard "merge two sorted linked lists" using a dummy head
        dummy = ListNode()   # sentinel node to simplify edge cases
        tail = dummy         # tail always points to last node in merged list

        # Walk both lists, always attach the smaller current node
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # advance the merged-list tail

        # One list is exhausted; attach whatever is left of the other
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Skip the dummy and return the real head
        return dummy.next
'''
Why pairwise merging?
A naive approach would merge lists one at a time:

First merge L0 + L1 → size n0+n1
Then merge that result with L2 → size n0+n1+n2
...and so on.
That costs O(N·k) in the worst case (each of the k merges can touch up to N nodes), which is too slow for k = 10000.

By merging in pairs, each level of the "merge tree" touches every node at most once, and there are log k levels. That's the difference between O(N·k) and O(N log k).

Trace through the example
Input: lists = [[1,2,4], [1,3,5], [3,6]]

Round 1 (pairs of 2):

merge([1,2,4], [1,3,5]) → [1,1,2,3,4,5]
merge([3,6], None) → [3,6] (odd list just passes through)
Result: [[1,1,2,3,4,5], [3,6]]

Round 2:

merge([1,1,2,3,4,5], [3,6]) → [1,1,2,3,3,4,5,6] ✅
Complexity Analysis
Let N = total number of nodes across all lists, k = number of lists.

Time O(N log k) log k rounds; each round touches each node once Space O(1) extra We only relink existing nodes — no new node allocations (besides the dummy/head sentinel)
Note: If you counted the call stack of mergeList recursively, you'd add O(log k) — but here mergeList is iterative, so extra space is truly O(1).

Common pitfalls
Odd number of lists → lists[i+1] would be out of bounds. The guard if (i + 1) < len(lists) handles this by passing None, and mergeList correctly returns just l1.
Empty input [] or [[]] → both are handled: [] returns immediately, and [[]] becomes a single None list that the while loop skips (since len == 1) and returns lists[0] = None.
Not using a dummy node in mergeList makes the code much messier — always use a sentinel when building linked lists.
Would you like me to also show the min-heap alternative (O(N log k) too, but different trade-offs)?

'''
        