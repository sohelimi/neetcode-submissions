'''Combination Sum - Problem Explanation
What's Being Asked?
You need to find all unique combinations of numbers from nums that add up to target. The key twist: each number can be used unlimited times.

Key Differences from Similar Problems:
✅ Can reuse numbers (unlike "2Sum")
✅ Need all combinations (not just count or one answer)
✅ Numbers are distinct, but combinations might use the same number multiple times
Approach: Backtracking/DFS
This is a classic backtracking problem. The idea:

Choose: Pick a number and add it to current combination
Explore: Recursively try to reach the target
Unchoose: Remove the number and try other options
Why backtracking? We need to explore all possibilities, then undo choices to try different paths.

Key Insight:
To avoid duplicate combinations (like [2,5] and [5,2]), we only move forward in the array. Once we pick index i, we can pick i again (reuse) or move to i+1.

Annotated Solution
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            # BASE CASE 1: Found a valid combination
            if total == target:
                res.append(cur.copy())  # cur.copy() important! Don't append reference
                return
            
            # BASE CASE 2: Invalid path - stop exploring
            if i >= len(nums) or total > target:
                return
            
            # CHOICE 1: Include nums[i] in combination
            # Stay at index i to allow reusing this number
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()  # Backtrack - remove choice
            
            # CHOICE 2: Skip nums[i], move to next number
            # This prevents duplicate combinations
            dfs(i + 1, cur, total)
        
        # Start DFS from index 0, empty combination, sum of 0
        dfs(0, [], 0)
        return res
'''
Walkthrough (Example 1: nums=[2,5,6,9], target=9)
                    dfs(0, [], 0)
                   /            \
            use 2 /              \ skip 2
            dfs(0,[2],2)         dfs(1,[],0)
            /         \          /        \
        use 2/       skip 2\   use 5/    skip 5\
        [2,2,4]     dfs(1,[2],2)  dfs(1,[5],5)  dfs(2,[],0)
                    /        \         |
                use 5/    skip 5\    use 5\
             [2,2,5]✓    dfs(2,[2],2) [5,5]=10✗
                          ...and so on
Complexity Analysis
Time: O(N^(T/M)) where N=len(nums), T=target, M=min(nums)

In worst case, we explore many branches
Space: O(T/M) for recursion depth (maximum numbers we can use to reach target)

Tips to Remember
cur.copy() - Must copy when adding to result (list is mutable reference)
Stay at index i to reuse numbers
Move to i+1 to skip and avoid duplicates
Check total > target early to prune invalid paths
Would you like me to trace through another example or explain any specific part deeper?
'''
        