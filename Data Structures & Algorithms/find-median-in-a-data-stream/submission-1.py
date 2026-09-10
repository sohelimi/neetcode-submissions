class MedianFinder:

    def __init__(self):
        # Max heap (invert values using negative)
        self.small = []  # max heap, stored as negatives
        self.large = []  # min heap


    def addNum(self, num: int) -> None:
        # Step 1: add to max heap (the smaller half)
        heapq.heappush(self.small, -num)

        # Step 2: balance so every element in small <= every element in large
        # If the largest element in small is greater than the smallest in large,
        # move one element from small to large to restore order.
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: balance sizes (keep the size difference <= 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd case: more elements in small
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Even case: average the two middle elements
        return (-self.small[0] + self.large[0]) / 2
        
'''
Here's what the code does, with commentary and some guidance.

What problem it solves

Maintains a dynamic set of numbers and can return the median at any time.
Uses two heaps (a max-heap for the smaller half, and a min-heap for the larger half) to keep the halves balanced.
Invariants:
All numbers in small (max-heap, stored as negatives) are <= all numbers in large (min-heap).
The sizes of the two heaps differ by at most 1.
If small has more elements, the median is the top of small; if they’re equal, the median is the average of the two tops.
Code walkthrough with comments

Important: ensure you import heapq at the top: import heapq


'''        