'''The Core Challenge
This is a variation of the classic House Robber problem, but with a circular constraint: the first and last houses are neighbors, so you can't rob both.

Why is this tricky?
In a linear arrangement, you can always consider robbing the first house or not. But here, your choice about the first house affects whether you can rob the last house.

The Strategy
The key insight: Break the circle into two linear problems

Since the first and last houses are the issue, consider these two scenarios:

Rob houses 0 to n-2 (exclude the last house) → This allows the first house
Rob houses 1 to n-1 (exclude the first house) → This allows the last house
Return the maximum of these two scenarios
For each linear scenario, use the standard House Robber DP approach:

At each house, decide: rob this house + best from 2 houses back, OR skip it
Track the maximum you can get up to each position
Completed Code with Comments
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house, rob it
        if len(nums) == 1:
            return nums[0]
        
        # Since houses are in a circle, first and last are neighbors
        # We can't rob both, so split into two scenarios:
        # Scenario 1: Rob from index 0 to n-2 (exclude last)
        # Scenario 2: Rob from index 1 to n-1 (exclude first)
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        """
        Standard linear house robber DP.
        rob1: max money we can get up to 2 houses ago
        rob2: max money we can get up to previous house
        """
        rob1, rob2 = 0, 0
        
        for n in nums:
            # At current house, take max of:
            # - Rob current house + what we had 2 houses back
            # - Skip current house and keep what we had
            newRob = max(rob1 + n, rob2)
            
            # Shift the pointers forward
            rob1 = rob2
            rob2 = newRob
        
        return rob2
'''
Complexity Analysis
Time: O(n) - We traverse the array up to 2 times
Space: O(1) - Only using two variables, not storing DP array
Example Walkthrough
For nums = [2, 9, 8, 3, 6]:

Scenario 1 (exclude index 4): [2, 9, 8, 3]

Rob 9 and 3 → Total: 12
Scenario 2 (exclude index 0): [9, 8, 3, 6]

Rob 9 and 6 → Total: 15

Result: max(12, 15) = 15 ✓
'''