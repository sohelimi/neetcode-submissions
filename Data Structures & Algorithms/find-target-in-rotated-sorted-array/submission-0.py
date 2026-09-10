'''
Solution Approach
The key insight is that even though the array is rotated, we can still use binary search by determining which half of the array is properly sorted and whether our target lies within that sorted half.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Target is in the right half
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Target is in the left half
                else:
                    right = mid - 1
        
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