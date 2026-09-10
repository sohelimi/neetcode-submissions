
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Store the best result found so far
        res = ""
        res_len = 0
        
        # Try every character as a potential palindrome center
        for i in range(len(s)):
            # Case 1: Odd-length palindromes (center is a single character)
            # Example: "aba" with center at index 1 ('b')
            left, right = i, i
            
            # Expand outward while characters match and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if this palindrome is longer than our current best
                current_len = right - left + 1
                if current_len > res_len:
                    res = s[left:right + 1]  # Update result - new string with new left and right
                    res_len = current_len     # Update length
                
                # Expand further
                left -= 1
                right += 1
            
            # Case 2: Even-length palindromes (center is between two characters)
            # Example: "bb" with center between indices 0 and 1
            left, right = i, i + 1
            
            # Expand outward while characters match and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if this palindrome is longer than our current best
                current_len = right - left + 1
                if current_len > res_len:
                    res = s[left:right + 1]  # Update result
                    res_len = current_len     # Update length
                
                # Expand further
                left -= 1
                right += 1
        
        return res


'''
Problem Understanding
You're given a string s and need to find the longest substring that is a palindrome.

Key Concepts
Palindrome: A string that reads the same forwards and backwards. Examples:

"racecar"
"madam"
"aba"
"bb"
Substring: A contiguous sequence of characters within the string.

Examples
s = "ababd"

Possible palindromes: "a", "b", "a", "b", "d", "aba", "bab"
Longest: "aba" or "bab" (both length 3)
Output: "bab" (or "aba")
s = "abbc"

Palindromes: "a", "b", "b", "c", "bb"
Longest: "bb" (length 2)
Challenge
The main difficulty is efficiently checking all possible substrings without brute force (which would be O(n³) if checking each substring naively).

Common Approaches
Expand Around Center (Most efficient for this problem):

Treat each character as the center of a palindrome
Expand outward while characters match
Handle both odd-length ("aba") and even-length ("bb") palindromes
Dynamic Programming:

Build a table to store palindrome information
More complex but systematic
Manacher's Algorithm:

O(n) time complexity
More advanced, usually not needed for interviews
Key Insight
Every palindrome has a center:

Odd-length: center is a single character ("aba" → center at 'b')
Even-length: center is between two characters ("bb" → center between the two 'b's)
Next Steps
Would you like me to:

Explain the "expand around center" approach in detail?
Walk through an example step by step?
Discuss time/space complexity?
See the code implementation?
This is a classic coding interview problem that tests your understanding of string manipulation and efficient algorithm design.

'''