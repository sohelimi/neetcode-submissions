class MedianFinder:

    def __init__(self):
        # Max heap (invert values using negative)
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: add to max heap
        heapq.heappush(self.small, -num)

        # Step 2: balance so every element in small <= large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd case
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Even case
        return (-self.small[0] + self.large[0]) / 2
        
        