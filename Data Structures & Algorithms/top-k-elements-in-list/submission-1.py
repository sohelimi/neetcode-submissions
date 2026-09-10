'''from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            bucket[c].append(num)
        res = []

        for i in range(len(sorted(bucket))):
            if i<=k:
                res[i].append(bucket[i])
            return res

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Step 1: Count frequencies
        count = Counter(nums)  # {num: freq}

        # Step 2: Create buckets — bucket[i] = list of numbers with frequency i
        # Max possible frequency is n, so we need n+1 buckets (index 0 to n)
        freq_bucket: List[List[int]] = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            freq_bucket[freq].append(num)  # place num in its frequency bucket

        # Step 3: Collect top k elements by scanning buckets from high to low frequency
        result: List[int] = []
        for freq in range(n, 0, -1):       # scan from highest freq to lowest
            for num in freq_bucket[freq]:  # add all nums at this frequency
                result.append(num)
                if len(result) == k:       # stop as soon as we have k elements
                    return result

        return result  # guaranteed k elements exist


        '''
        Solution Approach: Bucket Sort
This problem is solved using a bucket sort approach, which gives us O(n) time complexity.

Step-by-Step Explanation:
Count Frequencies (O(n)):

count = Counter(nums)  # {num: freq}
First, we count how many times each number appears. For example, nums = [1,2,2,3,3,3] gives {1:1, 2:2, 3:3}.

Create Frequency Buckets (O(n)):

freq_bucket: List[List[int]] = [[] for _ in range(n + 1)]
We create an array where the index represents frequency, and the value is a list of numbers with that frequency.

Why n + 1 buckets? Because the maximum possible frequency is n (if all elements are the same), so we need indices 0 through n.
Fill Buckets (O(n)):

for num, freq in count.items():
    freq_bucket[freq].append(num)
Place each number in the bucket corresponding to its frequency.

Collect Top K Elements (O(n)):

for freq in range(n, 0, -1):
    for num in freq_bucket[freq]:
        result.append(num)
        if len(result) == k:
            return result
We iterate from highest frequency to lowest, adding numbers to our result until we have k elements.

Why This Works:
Time Complexity: O(n) - we make three passes through the data
Space Complexity: O(n) - for the frequency map and buckets
Guarantees uniqueness: Since the answer is guaranteed to be unique, we don't need to handle ties
Issues in Your First Implementation:
sorted(bucket) creates a new sorted list, but you're using it for indexing
res[i].append(bucket[i]) tries to append a list to an integer position
The return statement is inside the loop, so it returns after first iteration
You're iterating from low to high frequency instead of high to low
Alternative Approaches:
Heap/Priority Queue (O(n log k)):

import heapq
count = Counter(nums)
return heapq.nlargest(k, count.keys(), key=count.get)
Quickselect (O(n) average case):
More complex but can be more efficient in practice for large datasets.

Your second implementation is the optimal O(n) solution and is exactly what's needed for coding interviews. The bucket sort approach is elegant because it leverages the fact that frequencies are bounded by n, allowing us to sort in linear time.
        '''

