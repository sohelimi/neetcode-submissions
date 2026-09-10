'''class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set[int](nums)
        best = 0
        length = 1

        for num in num_set:
            if (num-1) not in num_set:
                length = 1

            while (num+length) in num_set:
                length += 1 
            best = max(best, length)

        return best
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set to allow O(1) lookups and automatically remove duplicates
        num_set = set(nums)
        best = 0  # Tracks the length of the longest consecutive sequence found so far

        # Iterate over each unique number in the set
        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            # (i.e., 'num - 1' is not present in the set)
            if (num - 1) not in num_set:
                length = 1  # Start a new streak at current num
                # Check for next consecutive numbers in the sequence
                while (num + length) in num_set:
                    length += 1
                # Update the best length if we found a longer sequence
                best = max(best, length)

        # Return the length of the longest consecutive sequence found
        return best

