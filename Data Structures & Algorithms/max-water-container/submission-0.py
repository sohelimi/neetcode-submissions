class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Optimized O(n) solution using the two-pointer technique.

        We use two pointers (left and right), one starting at the beginning of the 
        array and the other at the end. The 'container' is formed by the lines at 
        these pointers, and the area they can contain is determined by the smaller 
        of the two heights times their distance apart. At each step, we move the 
        pointer pointing to the smaller height inward, since this is the only way 
        to potentially find a taller line that could increase the area.

        Args:
            height (List[int]): Heights of the vertical lines.

        Returns:
            int: Maximum area of water the container can store.
        """
        left = 0                            # Initialize the left pointer at the first index
        right = len(heights) - 1             # Initialize the right pointer at the last index
        max_area = 0                        # Track the largest area found

        # Continue until the two pointers meet
        while left < right:
            # The width is the horizontal distance between the pointers
            width = right - left
            
            # The height is determined by the shorter vertical line
            h = min(heights[left], heights[right])
            
            # Calculate the area with the current pair of lines
            area = h * width

            # Update max_area if we found a bigger one
            if area > max_area:
                max_area = area

            # Move the pointer at the shorter line inward,
            # since that's the only direction that might find a taller line 
            # (and thus potentially a larger area)
            if heights[left] < heights[right]:
                left += 1    # Move left pointer to the right
            else:
                right -= 1   # Move right pointer to the left

        return max_area