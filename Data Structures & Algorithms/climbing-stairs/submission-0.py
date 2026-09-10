class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # ways to reach step 1 and 2 respectively
        for _ in range(3, n + 1):
            a, b = b, a + b  # new = old1 + old2; shift window

        return b

'''
Here’s how to think about it.

What the problem asks

You have a staircase with n steps.
You can climb either 1 or 2 steps at a time.
How many distinct ways are there to reach exactly step n?
Key idea

The number of ways to reach step n depends on the ways to reach the previous steps:
If you take a 1-step from step n-1, you have ways(n-1) possibilities.
If you take a 2-steps from step n-2, you have ways(n-2) possibilities.
So, ways(n) = ways(n-1) + ways(n-2).
Base cases

ways(1) = 1
Only [1]
ways(2) = 2
[1,1], [2]
You can see the pattern: for n=3, ways(3) = 3 ( [1,1,1], [1,2], [2,1] ).
Relation to Fibonacci

This is the classic Fibonacci-like sequence with different starting values:
ways(1)=1, ways(2)=2, and for n>2, ways(n)=ways(n-1)+ways(n-2).
Approach options

Dynamic programming (iterative):
Compute from 1 up to n using the recurrence, storing only the last two values (O(1) space, O(n) time).
DP array (less space-efficient, but simple):
Keep an array dp[1..n], fill dp[i] = dp[i-1] + dp[i-2].
Recursive with memoization is possible but less efficient due to function call overhead (still O(n) time, O(n) space).
Edge cases

n is as small as 1, so handle base cases up front.
Given constraints n ≤ 45, the result fits in a 32-bit int.
A quick outline (iterative, O(1) space)

If n <= 2, return n.
Keep two variables:
a = ways(n-2) (start with 1 for n=2)
b = ways(n-1) (start with 2 for n=2)
For i from 3 to n:
c = a + b
a = b
b = c
Return b (which is ways(n)).
If you want, I can show the exact Python code using these ideas.
'''