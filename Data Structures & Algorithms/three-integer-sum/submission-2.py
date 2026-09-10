class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                current_sum = a + nums[l] + nums[r]
                if current_sum == 0:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1
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
