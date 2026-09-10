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