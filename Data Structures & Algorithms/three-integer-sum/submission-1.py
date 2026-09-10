'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We import List from the typing module to provide type hints for list parameters and return types.
        n = len(nums)
        found = set()  # use set to avoid duplicate triplets

        # Brute-force: try all possible triplets (i, j, k) with i < j < k
        # Collect unique triplets in a set by always sorting them first (avoids duplicates)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the current triplet sums to zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        found.add(triplet)  # Add to set for deduplication

        # Export: 'found' now holds all unique zero-sum triplets (as tuples)
        return [list(t) for t in found]
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array which gives the sum of zero.

        :param nums: List of integers
        :return: List of unique triplets [a, b, c] such that a + b + c == 0
        """
        nums.sort()  # Sort the input list to enable two-pointer approach and simplify duplicate handling
        result = []

        # Iterate through the list, fixing one number and finding the remaining two with two pointers
        for i in range(len(nums) - 2):  # Only go up to len(nums) - 2 because we need at least three numbers
            # If the current value is greater than 0, then further values will be greater (array is sorted),
            # so no need to proceed
            if nums[i] > 0:
                break

            # Skip duplicate fixed values to avoid duplicate triplets in result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Set two pointers
            while left < right:
                s = nums[left] + nums[right]  # Sum the two pointed values
                # Check if the sum with the fixed value equals zero
                if s == -nums[i]:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move left pointer to the next unique element to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move right pointer to the previous unique element to avoid duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers after recording a valid triplet
                    left += 1
                    right -= 1
                # If the sum is too small, move the left pointer to increase the sum
                elif s < -nums[i]:
                    left += 1
                # If the sum is too large, move the right pointer to decrease the sum
                else:
                    right -= 1

        return result  # Return the list of unique triplets    
