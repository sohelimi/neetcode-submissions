class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # ways to reach step 1 and 2 respectively
        for _ in range(3, n + 1):
            a, b = b, a + b  # new = old1 + old2; shift window

        return b

'''

'''