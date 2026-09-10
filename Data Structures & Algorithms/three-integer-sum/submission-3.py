from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Store all unique triplets found.
        res = []

        # Sort the array so that:
        # 1. We can use the two-pointer technique.
        # 2. Duplicate values are next to each other.
        # 3. We can avoid duplicate triplets easily.
        nums.sort()

        # Choose each number as the first number of a triplet.
        for i in range(len(nums)):
            # Since the array is sorted, if nums[i] is positive,
            # all numbers after it are also positive.
            # Therefore, a sum of three numbers cannot be zero.
            if nums[i] > 0:
                break

            # Skip duplicate values for the first number.
            # This prevents generating the same triplet multiple times.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # The first number in the current triplet.
            a = nums[i]

            # Use two pointers to find two numbers whose sum is -a.
            # Both pointers only consider indices after i, so all
            # three indices are distinct.
            l, r = i + 1, len(nums) - 1

            # Continue until the two pointers meet.
            while l < r:
                # Calculate the sum of the current three numbers.
                current_sum = a + nums[l] + nums[r]

                if current_sum == 0:
                    # We found a valid triplet.
                    res.append([a, nums[l], nums[r]])

                    # Move the left pointer forward.
                    l += 1

                    # Skip duplicate values for the second number.
                    # This prevents adding the same triplet again.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # We do not need to explicitly move r here.
                    # Since the array is sorted, increasing l after
                    # finding a zero sum would make the sum positive
                    # for the same r. The loop will eventually move r.
                
                elif current_sum > 0:
                    # The sum is too large.
                    # Since the array is sorted, decrease nums[r]
                    # by moving the right pointer left.
                    r -= 1

                else:
                    # The sum is too small.
                    # Increase nums[l] by moving the left pointer right.
                    l += 1

        # Return all unique triplets.
        return res

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Prepare the result list to collect unique triplets
        res = []
        # Sort the array to enable the two-pointer technique and easier duplicate skipping
        nums.sort()
        # Iterate over each number as the potential first element of the triplet
        for i in range(len(nums)):
            # Skip duplicates for the first element to avoid repeating triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Let 'a' be the current first element of the triplet
            a = nums[i]
            # Initialize two pointers: 'l' just right of i, and 'r' at the end of the array
            l, r = i + 1, len(nums) - 1
            # While the two pointers do not cross
            while l < r:
                # Compute the sum of the triplet candidates
                current_sum = a + nums[l] + nums[r]
                # If the sum is exactly zero, we found a valid triplet
                if current_sum == 0:
                    # Add the triplet to the result
                    res.append([a, nums[l], nums[r]])
                    # Move the left pointer forward to look for new pairs
                    l += 1
                    # Skip duplicates for the second element to avoid duplicates triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Note: We don't move 'r' here; typical implementations move both pointers and skip duplicates
                    # However, skipping duplicates on 'l' and the duplicate check on 'i' can still avoid duplicates
                # If the sum is too large, we need a smaller number, so move the right pointer leftward
                elif current_sum > 0:
                    r -= 1
                # If the sum is too small, we need a larger number, so move the left pointer rightward
                else:
                    l += 1
        # Return all non-duplicate triplets found
        return res
Notes:

Time complexity: O(n^2) in the worst case, due to the outer loop and the inner two-pointer scan.
Space complexity: O(1) extra space aside from the output, since the array is sorted in place (ignoring the output). If you count the output, it’s O(k) where k is the number of triplets found.
Optional improvement:

You can add an early break after sorting if nums[i] > 0, since further numbers will only increase the sum.
When you find a triplet (current_sum == 0), many solutions move both l and r and skip duplicates on both sides to be extra robust against duplicates. Your current approach skips duplicates on l; consider also moving and skipping duplicates on r for completeness.
'''
