'''House Robber Problem Explanation
Understanding the Problem
You need to maximize money stolen from houses with one constraint: you cannot rob two adjacent houses.

Think of it like this:

If you rob house i, you can't rob house i-1 or i+1
But you can rob house i and then skip to house i+2
Key Insight: Dynamic Programming
At each house, you have two choices:

Rob this house + the max money you could get from houses up to i-2
Skip this house + the max money you already have from houses up to i-1
You pick whichever gives more money.

Approach
Instead of storing an array of all previous results, we only need to track:

rob1: Max money robbed up to house i-2
rob2: Max money robbed up to house i-1
For each house, we calculate the max and shift our pointers forward.

Annotated Code
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents max money robbed up to i-2
        # rob2 represents max money robbed up to i-1
        rob1, rob2 = 0, 0

        for n in nums:
            # At current house n, we choose the maximum between:
            # 1. Rob current house (n) + max from 2 houses ago (rob1)
            # 2. Skip current house + max from previous house (rob2)
            temp = max(n + rob1, rob2)
            
            # Shift our window forward:
            # What was i-1 becomes i-2
            rob1 = rob2
            # What is current becomes i-1
            rob2 = temp
        
        # rob2 holds the maximum money we can rob from all houses
        return rob2
'''Example Walkthrough
For nums = [1,1,3,3]:

Start - 0 0 - - 0 1 0 max(1+0, 0)=1 Rob or skip Rob house 0 1 1 1 max(1+0, 1)=1 Rob or skip Skip house 1 2 3 1 max(3+1, 1)=4 Rob or skip Rob house 2 3 3 4 max(3+1, 4)=4 Rob or skip Skip house 3
Result: 4 (houses 0 and 2)

Complexity Analysis
Time Complexity: O(n) — single pass through the array
Space Complexity: O(1) — only two variables, no extra data structures
This is optimal! 🎯
'''