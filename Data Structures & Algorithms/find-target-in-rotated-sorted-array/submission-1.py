'''
Solution Approach
The key insight is that even though the array is rotated, we can still use binary search by determining which half of the array is properly sorted and whether our target lies within that sorted half.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start with the entire array as our search range.
        left = 0
        right = len(nums) - 1

        # Continue searching while the range is not empty.
        while left <= right:
            # Find the middle index of the current search range.
            mid = (left + right) // 2

            # If the middle element is the target, return its index.
            if nums[mid] == target:
                return mid

            # At least one half of the current range must be sorted.
            #
            # If nums[left] <= nums[mid], then the left half is sorted.
            if nums[left] <= nums[mid]:

                # Check whether the target falls inside the sorted
                # left half: [nums[left], nums[mid]).
                #
                # We already know nums[mid] is not the target,
                # so the upper bound is exclusive.
                if nums[left] <= target < nums[mid]:
                    # The target could be in the left half.
                    right = mid - 1
                else:
                    # The target is not in the sorted left half,
                    # so search the right half.
                    left = mid + 1

            # Otherwise, the right half must be sorted.
            else:

                # Check whether the target falls inside the sorted
                # right half: (nums[mid], nums[right]].
                #
                # We already know nums[mid] is not the target,
                # so the lower bound is exclusive.
                if nums[mid] < target <= nums[right]:
                    # The target could be in the right half.
                    left = mid + 1
                else:
                    # The target is not in the sorted right half,
                    # so search the left half.
                    right = mid - 1

        # The search range became empty, so the target is not present.
        return -1

'''        
Detailed Explanation
Core Idea
Even in a rotated sorted array, at least one half (left or right of the midpoint) will always be properly sorted. We can use this property to decide where to search next.

Step-by-Step Logic
Check which half is sorted:

If nums[left] <= nums[mid], the left half is sorted
Otherwise, the right half is sorted
If left half is sorted:

Check if target is within the sorted left half: nums[left] <= target < nums[mid]
If yes: search left (right = mid - 1)
If no: target must be in the right half (left = mid + 1)
If right half is sorted:

Check if target is within the sorted right half: nums[mid] < target <= nums[right]
If yes: search right (left = mid + 1)
If no: target must be in the left half (right = mid - 1)
Example Walkthrough
For nums = [3,4,5,6,1,2], target = 1:

left=0, right=5, mid=2 → nums[mid]=5

Left half [3,4,5] is sorted (3 ≤ 5)
Target 1 is NOT in [3,4,5] (1 < 3)
So search right: left=3
left=3, right=5, mid=4 → nums[mid]=1

Found target! Return 4
Time & Space Complexity
Time Complexity: O(log n) - We eliminate half the search space each iteration
Space Complexity: O(1) - We only use a few pointers
Why This Works
The rotation creates a "pivot point" where the array breaks. By checking which side is sorted, we can determine if our target could reasonably be on that side based on value comparisons, maintaining the O(log n) efficiency of binary search.
'''