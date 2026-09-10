'''
Problem Understanding
You're working with a rotated sorted array where all elements are unique. This means:

The array was originally sorted in ascending order (e.g., [1,2,3,4,5,6])
It was then rotated some number of times (1 to n times)
Rotation means taking elements from the end and moving them to the front
Key observation: After rotation, the array is divided into two sorted portions:

A larger sorted portion (earlier elements from the original array)
A smaller sorted portion (later elements from the original array)
Example: [4,5,6,7,0,1,2]

First portion: [4,5,6,7] (larger values)
Second portion: [0,1,2] (smaller values)
The minimum is at the start of the second portion
Your Code Analysis
Your current implementation is actually correct and optimal! Let me explain why:
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                #minimum is in right half
                left = mid + 1
            else:
                #minimum is in left half (including mid)
                right = mid
        return nums[left]

'''
How It Works:
Binary Search Setup: You use left and right pointers to search the array.

Key Comparison: You compare nums[mid] with nums[right]:

If nums[mid] > nums[right]: The minimum must be in the right half (after mid)

Why? Because in a rotated sorted array, if the middle is greater than the rightmost element, the rotation point (minimum) is between mid+1 and right
Example: [4,5,6,7,0,1,2], mid=7, right=2, 7>2 → min is in right half
Otherwise (nums[mid] <= nums[right]): The minimum is in the left half (including mid)

Why? Because the right portion is already sorted, so the minimum is at or before mid
Example: [4,5,0,1,2,3], mid=0, right=3, 0<=3 → min is in left half
Termination: When left == right, you've found the minimum element.

Time & Space Complexity:
Time: O(log n) - binary search halves the search space each iteration
Space: O(1) - only using a few pointers
Edge Cases Your Code Handles:
Already sorted array: [1,2,3,4,5] - correctly returns 1
Fully rotated array: [2,3,4,5,1] - correctly returns 1
Single element: [5] - returns 5
Two elements: [2,1] - returns 1
Why This Approach is Better Than O(n):
A naive O(n) solution would scan the entire array looking for the minimum. Your binary search approach is much more efficient for large arrays (logarithmic vs linear time).

Your implementation is clean, correct, and follows the optimal approach!
'''

