class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #position
        lpoint,rpoint = 0, 0 #first letter itself can be the longest
        uniq_char = set() 
        long_sub = 0 #initialize the longest set

        for rpoint in range(len(s)):
            while s[rpoint] in uniq_char:
                uniq_char.remove(s[lpoint])
                lpoint += 1

            uniq_char.add(s[rpoint])
            long_sub = max(long_sub, rpoint-lpoint+1)
            rpoint+=1
        return long_sub

'''
1. Z > not in uniq_char, so add it there
2. 
'''










'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chaar_set = set() 
        left = 0
        right = 0
        best = 0

        for right in range(len(s)):
            while s[right] in chaar_set:
                chaar_set.remove(s[left])
                left+=1

            chaar_set.add(s[right])
            best = max(best, right - left +1)
        return best
'''
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters
        using a sliding window and a set to track characters in the window.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        char_set = set()  # Holds unique characters currently in the window
        left = 0          # Left pointer of the window
        best = 0          # Stores the maximum length found

        # Iterate the right pointer across the string
        for right in range(len(s)):
            # If s[right] is already in the current set, 
            # shrink the window from the left until we remove the duplicate.
            while s[right] in char_set:
                # Remove the character at the left and move left pointer forward
                char_set.remove(s[left])
                left += 1

            # Now s[right] is unique in the window: add it
            char_set.add(s[right])

            # Update best if current window [left:right] is larger
            best = max(best, right - left + 1)

        return best
'''
        