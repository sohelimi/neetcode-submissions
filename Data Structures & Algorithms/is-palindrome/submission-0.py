class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                # If they don't match, it's not a palindrome
                return False

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If all characters matched, it's a palindrome
        return True