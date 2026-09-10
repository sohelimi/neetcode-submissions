class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store frequency of characters in current window
        count = {}
        
        # Left pointer of sliding window
        l = 0
        
        # Track the maximum frequency of any character in current window
        maxf = 0
        
        # Iterate through the string with right pointer
        for r in range(len(s)):
            # Update frequency of current character
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update max frequency - we only care about the maximum
            maxf = max(maxf, count[s[r]])
            
            # Check if current window is valid
            # Window length = (r - l + 1)
            # Characters to replace = window length - max frequency
            # If characters to replace > k, window is invalid
            if (r - l + 1) - maxf > k:
                # Shrink window from left
                count[s[l]] -= 1
                l += 1
        
        # At the end, the window size is our answer
        # Note: r is the last index from the loop
        return (len(s) - l)  # Equivalent to (r - l + 1) but handles edge cases
